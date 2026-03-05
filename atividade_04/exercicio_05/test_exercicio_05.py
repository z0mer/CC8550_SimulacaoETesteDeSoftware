from exercicio_05 import percorrer_matriz


def test_ambos_lacos_ignorados(capsys):
    # Cenário: m=0, n=0 → print executado 0 vezes (ambos os laços ignorados)
    percorrer_matriz(0, 0)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_laco_j_ignorado(capsys):
    # Cenário: m=1, n=0 → laço externo executa mas laço j ignorado → print 0 vezes
    percorrer_matriz(1, 0)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_laco_i_uma_vez_j_varias(capsys):
    # Cenário: m=1, n=3 → print executado 3 vezes
    percorrer_matriz(1, 3)
    captured = capsys.readouterr()
    linhas = captured.out.strip().split("\n")
    assert len(linhas) == 3
    assert linhas[0] == "Posicao (0, 0)"
    assert linhas[1] == "Posicao (0, 1)"
    assert linhas[2] == "Posicao (0, 2)"


def test_ambos_lacos_varias_vezes(capsys):
    # Cenário: m=3, n=3 → print executado 9 vezes
    percorrer_matriz(3, 3)
    captured = capsys.readouterr()
    linhas = captured.out.strip().split("\n")
    assert len(linhas) == 9


def test_laco_externo_varias_j_uma_vez(capsys):
    # Variação: m=3, n=1 → laço externo várias vezes, j uma vez → print 3 vezes
    percorrer_matriz(3, 1)
    captured = capsys.readouterr()
    linhas = captured.out.strip().split("\n")
    assert len(linhas) == 3
