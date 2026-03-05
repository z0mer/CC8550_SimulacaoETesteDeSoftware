# Exercício 6 – Teste Completo (Integrador)
#
# Grafo de Fluxo de Controle (GFC):
#
#   [1] Início / total=0
#        |
#   [2] n in numeros ? (laço for)
#      /              \
#    Sim              Não
#     |                |
#   [3] n>0 AND      [7] total > 10 ?
#       n%2==0 ?       /           \
#      /       \     Sim           Não
#    Sim        Não   |             |
#     |          |   [8] "Acima"  [9] "Abaixo"
#   [4]total+= [5] n<0?
#        |       /     \
#        |     Sim     Não
#        |      |       |
#        |  [6]total-=1 [continue]
#        |      |
#        +------+→ (volta para [2])
#
# Predicados: loop, n>0 AND n%2==0, n<0, total>10  →  V(G) ≈ 5
#
# Caminhos Independentes:
#   CP1: laço 0 iterações → total=0, total>10 falso → "Abaixo"
#   CP2: n par positivo (total ≤ 10) → "Abaixo"
#   CP3: n par positivo (total > 10) → "Acima"
#   CP4: n negativo → total -= 1 → "Abaixo"
#   CP5: n ímpar positivo (ou zero) → continue → "Abaixo"
#
# Pares def-uso de `total`:
#   def linha 2 (total=0)      → uso: total+=n, total-=1, total>10, return
#   def (total+=n)             → uso: total>10, return
#   def (total-=1)             → uso: total>10, return
#   def (total=total após if)  → uso: return


def analisar(numeros):
    total = 0
    for n in numeros:
        if n > 0 and n % 2 == 0:
            total += n
        elif n < 0:
            total -= 1
        else:
            continue
    if total > 10:
        return "Acima"
    return "Abaixo"
