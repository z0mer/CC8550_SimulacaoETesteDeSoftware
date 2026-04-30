"""
Testes de Escalabilidade — ThreadPoolExecutor
Meta: eficiência de escalonamento horizontal > 80%.

Simula múltiplos workers (servidores) processando requisições em paralelo.
O time.sleep(0.001) no service libera o GIL do Python durante a espera de I/O,
permitindo que threads genuinamente concorrentes demonstrem ganho real de throughput.
"""
import time
import concurrent.futures
import pytest

N_REQUESTS = 200


def _medir_throughput(service, n_workers: int) -> float:
    inicio = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = [
            executor.submit(service.listar_produtos)
            for _ in range(N_REQUESTS)
        ]
        concurrent.futures.wait(futures)
    duracao = time.perf_counter() - inicio
    return N_REQUESTS / duracao


class TestEscalabilidade:
    def test_throughput_aumenta_com_4_workers(self, produto_service):
        for i in range(10):
            produto_service.cadastrar_produto(f"Produto {i}", float(i + 1) * 10, 100)

        throughput_1 = _medir_throughput(produto_service, n_workers=1)
        throughput_4 = _medir_throughput(produto_service, n_workers=4)

        eficiencia = (throughput_4 / throughput_1) / 4.0
        assert eficiencia >= 0.80, (
            f"Eficiência com 4 workers: {eficiencia:.1%} — abaixo da meta de 80%\n"
            f"  Throughput 1 worker: {throughput_1:.1f} req/s\n"
            f"  Throughput 4 workers: {throughput_4:.1f} req/s"
        )

    def test_sem_degradacao_sob_carga_8_workers(self, produto_service):
        for i in range(10):
            produto_service.cadastrar_produto(f"Produto {i}", float(i + 1) * 10, 100)

        throughput_1 = _medir_throughput(produto_service, n_workers=1)
        throughput_8 = _medir_throughput(produto_service, n_workers=8)

        assert throughput_8 >= throughput_1 * 0.80, (
            f"Throughput com 8 workers ({throughput_8:.1f} req/s) < 80% "
            f"do throughput com 1 worker ({throughput_1:.1f} req/s)"
        )

    def test_estabilidade_throughput_carga_sustentada(self, produto_service):
        for i in range(10):
            produto_service.cadastrar_produto(f"Produto {i}", float(i + 1) * 10, 100)

        def run_batch(n: int) -> float:
            inicio = time.perf_counter()
            for _ in range(n):
                produto_service.listar_produtos()
            return n / (time.perf_counter() - inicio)

        tp_primeiro = run_batch(100)
        tp_segundo = run_batch(100)

        assert tp_segundo >= tp_primeiro * 0.80, (
            f"Degradação detectada: primeira metade {tp_primeiro:.1f} req/s, "
            f"segunda metade {tp_segundo:.1f} req/s"
        )
