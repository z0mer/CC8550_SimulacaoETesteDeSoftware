from exercicio_06 import analisar


def test_laco_zero_iteracoes():
    # CP1: laço 0 iterações → total=0 → "Abaixo"
    assert analisar([]) == "Abaixo"


def test_laco_uma_iteracao_par_positivo_abaixo():
    # CP2: [2] → total=2 ≤ 10 → "Abaixo"
    assert analisar([2]) == "Abaixo"


def test_laco_varias_iteracoes_acima():
    # CP3: [2,4,6] → total=12 > 10 → "Acima"
    assert analisar([2, 4, 6]) == "Acima"


def test_laco_negativo():
    # CP4: [-1] → total=-1 → "Abaixo"
    assert analisar([-1]) == "Abaixo"


def test_laco_impar_positivo_continue():
    # CP5: [1] → ímpar positivo → continue → total=0 → "Abaixo"
    assert analisar([1]) == "Abaixo"
