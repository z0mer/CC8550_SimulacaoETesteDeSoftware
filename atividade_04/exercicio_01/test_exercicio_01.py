from exercicio_01 import verificar


def test_caminho1_par_positivo():
    # Caminho 1: n > 0 e n % 2 == 0 → "Par positivo"
    assert verificar(4) == "Par positivo"


def test_caminho2_impar_positivo():
    # Caminho 2: n > 0 e n % 2 != 0 → "Impar positivo"
    assert verificar(3) == "Impar positivo"


def test_caminho3_negativo():
    # Caminho 3: n < 0 → "Negativo"
    assert verificar(-1) == "Negativo"


def test_caminho4_zero():
    # Caminho 4: n == 0 → "Zero"
    assert verificar(0) == "Zero"
