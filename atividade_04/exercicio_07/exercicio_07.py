# Exercício 7 – Fluxo de Dados
#
# Código fonte com numeração de linhas:
#   L1: def desconto(preco, cliente_vip):
#   L2:     total = preco                   ← def total (1)
#   L3:     if cliente_vip:
#   L4:         desconto = preco * 0.2      ← def desconto_var
#   L5:         total = preco - desconto    ← def total (2); uso desconto_var
#   L6:     if total < 50:                  ← uso total
#   L7:         total = 50                  ← def total (3)
#   L8:     return total                    ← uso total
#
# Definições e usos de cada variável:
#   preco       : def L1; uso L2, L4, L5
#   cliente_vip : def L1; uso L3
#   total       : def L2, L5, L7; uso L6, L8
#   desconto    : def L4; uso L5
#
# Pares def-uso de `total`:
#   (L2, L6): total=preco usado em if total < 50
#   (L2, L8): total=preco usado em return (quando cliente_vip=False e total>=50)
#   (L5, L6): total=preco-desconto usado em if total < 50
#   (L5, L8): total=preco-desconto usado em return (quando cliente_vip=True e total>=50)
#   (L7, L8): total=50 usado em return
#
# Casos de Teste para All-Defs (cobrir cada def de total ao menos uma vez):
#   CT-AD1: preco=100, cliente_vip=False → total=100 (def L2 usada em L6, L8)
#   CT-AD2: preco=100, cliente_vip=True  → total=80  (def L5 usada em L6, L8)
#   CT-AD3: preco=30,  cliente_vip=False → total=50  (def L7 usada em L8)
#
# Casos de Teste para All-Uses (cobrir cada par def-uso):
#   CT-AU1 (L2,L6)+(L2,L8): preco=100, cliente_vip=False → total=100 ≥ 50 → return 100
#   CT-AU2 (L2,L6)+(L7,L8): preco=30,  cliente_vip=False → total=30 < 50 → total=50 → return 50
#   CT-AU3 (L5,L6)+(L5,L8): preco=100, cliente_vip=True  → total=80 ≥ 50 → return 80
#   CT-AU4 (L5,L6)+(L7,L8): preco=30,  cliente_vip=True  → total=24 < 50 → total=50 → return 50
#
# Par def-uso não coberto por C1 sozinho:
#   O par (L5, L8) — cliente_vip=True e total>=50 (ex: preco=100) — exige
#   que o segundo if seja False, o que nem sempre é garantido pelos CTs de C1
#   que apenas verificam True/False de cada if isoladamente.


def desconto(preco, cliente_vip):
    total = preco
    if cliente_vip:
        desconto_var = preco * 0.2
        total = preco - desconto_var
    if total < 50:
        total = 50
    return total
