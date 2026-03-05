from exercicio_03 import acesso


def test_cc_idade_maior_e_membro_true():
    # CC – CT1: idade >= 18 (True) e membro (True) → "Permitido"
    assert acesso(20, True) == "Permitido"


def test_cc_idade_maior_e_membro_false():
    # CC – CT2: idade >= 18 (True) e membro (False) → "Negado"
    assert acesso(20, False) == "Negado"


def test_cc_idade_menor_e_membro_true():
    # CC – CT3: idade >= 18 (False) e membro (True) → "Negado"
    assert acesso(16, True) == "Negado"


def test_cc_idade_menor_e_membro_false():
    # CC – CT4: idade >= 18 (False) e membro (False) → "Negado"
    assert acesso(16, False) == "Negado"


def test_c1_ramo_verdadeiro():
    # C1 – ramo Sim: condição composta True → "Permitido"
    assert acesso(18, True) == "Permitido"


def test_c1_ramo_falso():
    # C1 – ramo Não: condição composta False → "Negado"
    assert acesso(17, True) == "Negado"
