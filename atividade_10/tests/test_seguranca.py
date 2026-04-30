"""
Testes de Segurança — Rate Limiting
Meta: 100 req/min por IP; requisições acima do limite retornam HTTP 429.

Usa o test client do Flask (sem servidor externo), permitindo rodar como pytest comum.
O Flask-Limiter com storage_uri="memory://" mantém o estado de rate limiting entre
chamadas dentro do mesmo test client, simulando requisições do mesmo IP.
"""
import pytest


class TestRateLimitingSaude:
    def test_saude_nao_e_limitado(self, flask_client):
        """Endpoint de saúde não possui rate limit — deve sempre retornar 200."""
        for _ in range(10):
            resp = flask_client.get("/saude")
            assert resp.status_code == 200


class TestRateLimitingProdutos:
    def test_primeiras_requisicoes_sao_permitidas(self, flask_client):
        """As primeiras 5 requisições devem retornar 200."""
        for _ in range(5):
            resp = flask_client.get("/produtos")
            assert resp.status_code == 200

    def test_rate_limit_retorna_429_apos_100_requisicoes(self, flask_client):
        """Após 100 requisições no mesmo minuto, a 101ª deve retornar 429."""
        codigos = []
        for _ in range(105):
            resp = flask_client.get("/produtos")
            codigos.append(resp.status_code)

        assert 429 in codigos, (
            "Rate limit de 100 req/min não foi ativado — nenhum 429 recebido em 105 requisições"
        )

    def test_rate_limit_inclui_header_retry_after(self, flask_client):
        """Resposta 429 deve incluir header Retry-After ou X-RateLimit-Reset."""
        ultima_resposta_429 = None
        for _ in range(105):
            resp = flask_client.get("/produtos")
            if resp.status_code == 429:
                ultima_resposta_429 = resp
                break

        assert ultima_resposta_429 is not None, "Nenhuma resposta 429 recebida"
        headers = {k.lower() for k in ultima_resposta_429.headers.keys()}
        assert "retry-after" in headers or "x-ratelimit-reset" in headers, (
            f"Headers de rate limit ausentes. Headers recebidos: {list(ultima_resposta_429.headers.keys())}"
        )


class TestRateLimitingPedidos:
    def test_pedidos_tambem_e_limitado(self, flask_client):
        """POST /pedidos também deve aplicar rate limiting."""
        codigos = []
        for _ in range(105):
            resp = flask_client.post("/pedidos", json={"itens": []})
            codigos.append(resp.status_code)

        assert 429 in codigos, (
            "Rate limit não foi ativado no endpoint POST /pedidos"
        )


class TestIsolamentoDeLimites:
    def test_limite_de_produtos_nao_afeta_saude(self, flask_client):
        """Esgotar o rate limit de /produtos não deve bloquear o endpoint /saude."""
        for _ in range(105):
            flask_client.get("/produtos")

        resp = flask_client.get("/saude")
        assert resp.status_code == 200, (
            "O endpoint /saude foi bloqueado indevidamente após atingir o limite de /produtos"
        )
