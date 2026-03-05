# Exercício 1 – Caminhos Independentes
#
# Grafo de Fluxo de Controle (GFC):
#
#   [1] Início / entrada de n
#        |
#   [2] n > 0 ?
#      /       \
#    Sim        Não
#     |          |
#   [3] n%2==0? [6] n < 0 ?
#    /    \       /     \
#  Sim    Não   Sim     Não
#   |      |     |       |
#  [4]    [5]   [7]     [8]
# "Par  "Impar "Neg." "Zero"
# pos." pos."
#
# Nós: 8 (1=entrada, 2=n>0, 3=n%2==0, 4=Par pos., 5=Impar pos., 6=n<0, 7=Negativo, 8=Zero)
# Arestas: 10
# Predicados: 3  →  V(G) = predicados + 1 = 4
# (ou V(G) = E - N + 2P = 10 - 8 + 2 = 4)
#
# Caminhos Independentes:
#   Caminho 1: 1→2(Sim)→3(Sim)→4     n > 0 e par    → "Par positivo"
#   Caminho 2: 1→2(Sim)→3(Não)→5     n > 0 e ímpar  → "Impar positivo"
#   Caminho 3: 1→2(Não)→6(Sim)→7     n < 0          → "Negativo"
#   Caminho 4: 1→2(Não)→6(Não)→8     n == 0         → "Zero"


def verificar(n):
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
