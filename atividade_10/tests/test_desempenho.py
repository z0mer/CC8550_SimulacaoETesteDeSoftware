"""
Testes de Desempenho — pytest-benchmark
Meta: P95 (aproximado pela média) < 500ms por operação na camada de serviço.

Os testes operam diretamente sobre a camada de serviço (sem HTTP) para eliminar
ruído de rede e medir com precisão o comportamento algorítmico.
"""
import pytest


class TestDesempenhoListarProdutos:
    @pytest.mark.benchmark(min_rounds=100)
    def test_p95_listar_produtos_vazio(self, benchmark, produto_service):
        resultado = benchmark(produto_service.listar_produtos)
        assert benchmark.stats["mean"] < 0.5, (
            f"Média {benchmark.stats['mean']*1000:.2f}ms excede SLA de 500ms"
        )

    @pytest.mark.benchmark(min_rounds=100)
    def test_p95_listar_produtos_50_itens(self, benchmark, produto_service):
        for i in range(50):
            produto_service.cadastrar_produto(f"Produto BF {i:02d}", 10.0 * (i + 1), 100)

        benchmark(produto_service.listar_produtos)
        assert benchmark.stats["mean"] < 0.5, (
            f"Média {benchmark.stats['mean']*1000:.2f}ms excede SLA de 500ms com 50 produtos"
        )


class TestDesempenhoBuscarProduto:
    @pytest.mark.benchmark(min_rounds=100)
    def test_p95_buscar_produto_por_id(self, benchmark, produto_service, produto_populado):
        resultado = benchmark(produto_service.buscar_produto, produto_populado.id)
        assert benchmark.stats["mean"] < 0.5, (
            f"Média {benchmark.stats['mean']*1000:.2f}ms excede SLA de 500ms"
        )


class TestDesempenhoCriarPedido:
    @pytest.mark.benchmark(min_rounds=50)
    def test_p95_criar_pedido(self, benchmark, pedido_service, produto_populado):
        itens = [{"produto_id": produto_populado.id, "quantidade": 1}]
        benchmark(pedido_service.criar_pedido, itens)
        assert benchmark.stats["mean"] < 0.5, (
            f"Média {benchmark.stats['mean']*1000:.2f}ms excede SLA de 500ms"
        )


class TestDesempenhoCadastrarProduto:
    @pytest.mark.benchmark(min_rounds=100)
    def test_p95_cadastrar_produto(self, benchmark, produto_service):
        benchmark(produto_service.cadastrar_produto, "Produto Benchmark", 99.90, 500)
        assert benchmark.stats["mean"] < 0.5, (
            f"Média {benchmark.stats['mean']*1000:.2f}ms excede SLA de 500ms"
        )
