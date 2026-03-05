# Exercício 3 – Cobertura de Condição
#
# Grafo de Fluxo de Controle (GFC):
#
#   [1] Início / entrada de idade, membro
#        |
#   [2] (idade >= 18) AND membro ?
#      /                          \
#    Sim                          Não
#     |                            |
#   [3] "Permitido"            [4] "Negado"
#
# Nós: 4
# Arestas: 4
# Predicados: 1  →  V(G) = predicados + 1 = 2
# (ou V(G) = E - N + 2P = 4 - 4 + 2 = 2)
#
# Caminhos Independentes:
#   Caminho 1: 1→2(Sim)→3      condição composta verdadeira → "Permitido"
#   Caminho 2: 1→2(Não)→4      condição composta falsa      → "Negado"
#
# Cobertura de Condição (CC) – todas as combinações das subcondições:
#   | idade >= 18 | membro | Resultado  |
#   |-------------|--------|------------|
#   | True        | True   | Permitido  |  ← CT1
#   | True        | False  | Negado     |  ← CT2
#   | False       | True   | Negado     |  ← CT3
#   | False       | False  | Negado     |  ← CT4
#
# Cobertura de Ramos (C1): apenas 2 CTs (True/False do if composto).
#
# Diferença: CC exige 4 CTs para explorar todos os valores das subcondições
# individualmente; C1 exige apenas 2. CC é mais rigorosa.


def acesso(idade, membro):
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"
