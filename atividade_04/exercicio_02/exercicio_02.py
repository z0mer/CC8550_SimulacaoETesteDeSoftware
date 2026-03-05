# Exercício 2 – Cobertura de Comandos e Ramos
#
# Grafo de Fluxo de Controle (GFC):
#
#   [1] Início / entrada de x
#        |
#   [2] x > 100 ?
#      /        \
#    Sim        Não
#     |          |
#   [3] "Alto"  [4] x > 50 ?
#                /         \
#              Sim          Não
#               |            |
#             [5] "Medio"  [6] "Baixo"
#
# Nós: 6
# Arestas: 7
# Predicados: 2  →  V(G) = predicados + 1 = 3
# (ou V(G) = E - N + 2P = 7 - 6 + 2 = 3)
#
# Caminhos Independentes:
#   Caminho 1: 1→2(Sim)→3              x > 100        → "Alto"
#   Caminho 2: 1→2(Não)→4(Sim)→5      50 < x ≤ 100   → "Medio"
#   Caminho 3: 1→2(Não)→4(Não)→6      x ≤ 50         → "Baixo"
#
# Cobertura C0 (comandos):
#   São necessários 3 CTs para executar os três return distintos.
#
# Cobertura C1 (ramos):
#   São necessários 3 CTs para exercitar os ramos Sim/Não de cada if.
#   Os mesmos 3 CTs que cobrem C1 também cobrem C0.


def classificar(x):
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"
