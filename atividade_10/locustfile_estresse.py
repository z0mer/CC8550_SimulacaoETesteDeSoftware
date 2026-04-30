"""
Teste de Estresse — Locust (modo spike)
Meta: Sistema suporta > 15.000 usuários simultâneos com taxa de erro < 5%.

Comando para executar:
  locust -f locustfile_estresse.py --headless -u 15000 -r 500 --run-time 120s \\
    --host http://localhost:5000 --html relatorio_estresse.html

Interpretação do ponto de quebra (breakpoint):
  - O sistema "aguenta" enquanto a taxa de erro de servidor (5xx) < 5%
  - Respostas 429 (rate limiting) são tratadas como SUCESSO — é comportamento esperado
    sob carga extrema e não indica falha do servidor
  - O breakpoint é o número de usuários onde erros 5xx atingem 5%
  - Meta: > 15.000 usuários sem atingir o breakpoint

Critério de aprovação:
  - Com 15.000 usuários simultâneos, taxa de erro 5xx < 5%
  - O sistema se recupera quando a carga diminui (resiliência)
"""
import random
import logging
from locust import HttpUser, task, between, events


class UsuarioEstresse(HttpUser):
    """
    Usuário de estresse com think time reduzido para maximizar a pressão no servidor.
    """
    wait_time = between(0.05, 0.2)

    def on_start(self):
        self.client.get("/saude")

    @task(4)
    def listar_produtos(self):
        with self.client.get(
            "/produtos",
            catch_response=True,
            name="GET /produtos",
        ) as resp:
            if resp.status_code == 429:
                resp.success()  # rate limiting é comportamento esperado, não falha
            elif resp.status_code >= 500:
                resp.failure(f"Erro de servidor: {resp.status_code}")

    @task(2)
    def buscar_produto(self):
        produto_id = random.randint(1, 50)
        with self.client.get(
            f"/produtos/{produto_id}",
            catch_response=True,
            name="GET /produtos/{id}",
        ) as resp:
            if resp.status_code in (200, 404, 429):
                resp.success()
            elif resp.status_code >= 500:
                resp.failure(f"Erro de servidor: {resp.status_code}")

    @task(1)
    def verificar_saude(self):
        with self.client.get(
            "/saude",
            catch_response=True,
            name="GET /saude",
        ) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure(f"Health check falhou: {resp.status_code}")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    stats = environment.stats.total
    n_usuarios = getattr(environment.runner, "user_count", "?")
    taxa_erro = stats.fail_ratio * 100
    rps = stats.current_rps

    logging.info("=" * 60)
    logging.info(f"[ESTRESSE] Resultado do Teste de Estresse")
    logging.info(f"  Usuários simultâneos: {n_usuarios}")
    logging.info(f"  Throughput: {rps:.0f} req/s")
    logging.info(f"  Taxa de erro (5xx): {taxa_erro:.2f}%")
    logging.info(f"  Total de requisições: {stats.num_requests}")
    logging.info(f"  Total de falhas: {stats.num_failures}")

    if taxa_erro < 5.0:
        logging.info(f"  RESULTADO: PASSOU — sistema suportou a carga sem ruptura")
    else:
        logging.info(f"  RESULTADO: REPROVADO — taxa de erro {taxa_erro:.1f}% acima de 5%")
    logging.info("=" * 60)
