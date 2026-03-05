from exercicio_02 import classificar


def test_caminho1_alto():
    # Caminho 1 | C0+C1: x > 100 → "Alto"
    assert classificar(150) == "Alto"


def test_caminho2_medio():
    # Caminho 2 | C0+C1: 50 < x ≤ 100 → "Medio"
    assert classificar(75) == "Medio"


def test_caminho3_baixo():
    # Caminho 3 | C0+C1: x ≤ 50 → "Baixo"
    assert classificar(30) == "Baixo"


def test_fronteira_exato_100():
    # Valor limite: x == 100 → não entra no primeiro if → "Medio"
    assert classificar(100) == "Medio"


def test_fronteira_exato_50():
    # Valor limite: x == 50 → não entra no segundo if → "Baixo"
    assert classificar(50) == "Baixo"
