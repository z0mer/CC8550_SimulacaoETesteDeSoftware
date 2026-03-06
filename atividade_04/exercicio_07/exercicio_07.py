def desconto(preco, cliente_vip):
    total = preco
    if cliente_vip:
        desconto_var = preco * 0.2
        total = preco - desconto_var
    if total < 50:
        total = 50
    return total
