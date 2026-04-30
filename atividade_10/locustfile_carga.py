"""
Teste de Carga — Locust
Meta: Throughput sustentado > 2.000 req/s com múltiplos usuários simultâneos.

Comando para executar:
  locust -f locustfile_carga.py --headless -u 500 -r 50 --run-time 60s \\
    --host http://localhost:5000 --html relatorio_carga.html

Para maior capacidade (produção), substituir o servidor Flask por:
  gunicorn -w 4 -b 0.0.0.0:5000 app:app

Critério de aprovação:
  - Throughput médio >= 2.000 req/s durante a janela de 60s
  - Taxa de erro < 1%
  - P95 de tempo de resposta < 500ms
"""
import random
from locust import HttpUser, task, between


class UsuarioBlackFriday(HttpUser):
    """
    Simula o comportamento de um usuário navegando e comprando durante a Black Friday.
    Distribuição de tarefas reflete o padrão real de tráfego de e-commerce:
    - Navegação no catálogo é a ação mais frequente (peso 5 + 3)
    - Adição ao carrinho é intermediária (peso 2)
    - Criação de pedido é a menos frequente (peso 1)
    """
    wait_time = between(0.1, 0.5)

    def on_start(self):
        resp = self.client.get("/saude")
        if resp.status_code != 200:
            self.environment.runner.quit()

    @task(5)
    def listar_produtos(self):
        self.client.get("/produtos", name="GET /produtos")

    @task(3)
    def buscar_produto(self):
        produto_id = random.randint(1, 50)
        self.client.get(f"/produtos/{produto_id}", name="GET /produtos/{id}")

    @task(2)
    def adicionar_carrinho(self):
        payload = {
            "produto_id": random.randint(1, 50),
            "quantidade": random.randint(1, 3),
        }
        self.client.post("/carrinho", json=payload, name="POST /carrinho")

    @task(1)
    def criar_pedido(self):
        payload = {
            "itens": [
                {"produto_id": random.randint(1, 50), "quantidade": random.randint(1, 2)}
            ]
        }
        self.client.post("/pedidos", json=payload, name="POST /pedidos")

    @task(1)
    def verificar_saude(self):
        self.client.get("/saude", name="GET /saude")
