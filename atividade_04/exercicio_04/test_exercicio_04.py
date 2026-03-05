from exercicio_04 import somar_ate


def test_laco_ignorado():
    # Caminho 1: n=0 → laço não executa → soma=0
    assert somar_ate(0) == 0


def test_laco_uma_vez():
    # Caminho 2 (1 iteração): n=1 → range(1)=[0] → soma=0
    assert somar_ate(1) == 0


def test_laco_varias_vezes():
    # Caminho 2 (várias iterações): n=5 → 0+1+2+3+4=10
    assert somar_ate(5) == 10


def test_laco_duas_vezes():
    # Variação: n=2 → 0+1=1
    assert somar_ate(2) == 1
