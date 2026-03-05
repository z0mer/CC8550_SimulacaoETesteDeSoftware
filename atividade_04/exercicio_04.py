# Exercício 4 – Teste de Ciclo
#
# Grafo de Fluxo de Controle (GFC):
#
#   [1] Início / soma = 0
#        |
#   [2] i < n ? (condição do for/range)
#      /        \
#    Sim        Não
#     |          |
#   [3] soma+=i [4] return soma
#     |
#   (volta para [2])
#
# Nós: 4
# Arestas: 5
# Predicados: 1  →  V(G) = predicados + 1 = 2
# (ou V(G) = E - N + 2P = 5 - 4 + 2 = 3, considerando o back-edge do laço)
#
# Caminhos Independentes:
#   Caminho 1: 1→2(Não)→4      laço ignorado (n=0)
#   Caminho 2: 1→2(Sim)→3→2→4  laço executado (n≥1)
#
# Casos de Teste:
#   n=0 → soma=0         (laço ignorado)
#   n=1 → soma=0         (laço 1 vez: range(1)=[0], 0+0=0)
#   n=5 → soma=10        (laço várias vezes: 0+1+2+3+4=10)


def somar_ate(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma


# ---------------------------------------------------------------------------
# Casos de Teste
# ---------------------------------------------------------------------------

def test_laco_ignorado():
    # Caminho 1: n=0 → laço não executa → soma=0
    assert somar_ate(0) == 0


def test_laco_uma_vez():
    # Caminho 2 (1 iteração): n=1 → range(1)=[0] → soma=0
    assert somar_ate(1) == 0


def test_laco_varias_vezes():
    # Caminho 2 (várias iterações): n=5 → 0+1+2+3+4=10
    assert somar_ate(5) == 10


def test_laco_duas_vezes():
    # Variação: n=2 → 0+1=1
    assert somar_ate(2) == 1
