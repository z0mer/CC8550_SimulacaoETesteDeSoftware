from exercicio_07 import desconto


def test_all_defs_sem_vip_preco_alto():
    # CT-AD1 | All-Defs def(L2): preco=100, cliente_vip=False → return 100
    assert desconto(100, False) == 100


def test_all_defs_com_vip_preco_alto():
    # CT-AD2 | All-Defs def(L5): preco=100, cliente_vip=True → total=80 → return 80
    assert desconto(100, True) == 80


def test_all_defs_sem_vip_preco_baixo():
    # CT-AD3 | All-Defs def(L7): preco=30, cliente_vip=False → total=30<50 → total=50 → return 50
    assert desconto(30, False) == 50


def test_all_uses_du_L2_L6_L2_L8():
    # CT-AU1 | All-Uses (L2,L6)+(L2,L8): preco=100, cliente_vip=False → return 100
    assert desconto(100, False) == 100


def test_all_uses_du_L2_L6_L7_L8():
    # CT-AU2 | All-Uses (L2,L6)+(L7,L8): preco=30, cliente_vip=False → return 50
    assert desconto(30, False) == 50


def test_all_uses_du_L5_L6_L5_L8():
    # CT-AU3 | All-Uses (L5,L6)+(L5,L8): preco=100, cliente_vip=True → total=80 → return 80
    assert desconto(100, True) == 80


def test_all_uses_du_L5_L6_L7_L8():
    # CT-AU4 | All-Uses (L5,L6)+(L7,L8): preco=30, cliente_vip=True → total=24<50 → return 50
    assert desconto(30, True) == 50


def test_fronteira_total_igual_50():
    # Valor limite: total==50 → segundo if False → return 50 sem modificação
    assert desconto(50, False) == 50


def test_fronteira_total_abaixo_50_com_vip():
    # preco=60, cliente_vip=True → total=48 < 50 → total=50 → return 50
    assert desconto(60, True) == 50
