import pytest
from hypothesis import given, strategies as st

from frete import calcular_frete


# 1) Classes de Equivalência (5 casos)
@pytest.mark.parametrize(
    "peso,destino,valor_pedido,esperado",
    [
        (0.5, "mesma_regiao", 100.0, 10.0),
        (3.0, "mesma_regiao", 100.0, 15.0),
        (10.0, "mesma_regiao", 100.0, 25.0),
        (10.0, "outra_regiao", 100.0, 37.5),
        (10.0, "internacional", 100.0, 50.0),
    ],
)
def test_classes_equivalencia(peso, destino, valor_pedido, esperado):
    assert calcular_frete(peso, destino, valor_pedido) == esperado


# 2) Valores Limite (9 casos - fronteiras: 1, 5, 20)
@pytest.mark.parametrize(
    "peso,esperado",
    [
        (0.99, 10.0),
        (1.0, 10.0),
        (1.01, 15.0),
        (4.99, 15.0),
        (5.0, 15.0),
        (5.01, 25.0),
        (19.99, 25.0),
        (20.0, 25.0),
        (20.01, None),
    ],
)
def test_valores_limite_peso(peso, esperado):
    if esperado is None:
        with pytest.raises(ValueError):
            calcular_frete(peso, "mesma_regiao", 100.0)
    else:
        assert calcular_frete(peso, "mesma_regiao", 100.0) == esperado


# 3) Tabela de Decisão (6 regras)
def test_tabela_decisao_mesma_regiao_sem_acrescimo():
    assert calcular_frete(1.0, "mesma_regiao", 100.0) == 10.0


def test_tabela_decisao_outra_regiao_mais_50_porcento():
    assert calcular_frete(5.0, "outra_regiao", 100.0) == 22.5


def test_tabela_decisao_internacional_mais_100_porcento():
    assert calcular_frete(5.0, "internacional", 100.0) == 30.0


def test_tabela_decisao_pedido_acima_200_frete_gratis():
    assert calcular_frete(5.0, "internacional", 201.0) == 0.0


def test_tabela_decisao_peso_zero_erro():
    with pytest.raises(ValueError):
        calcular_frete(0.0, "mesma_regiao", 100.0)


def test_tabela_decisao_peso_acima_20_erro():
    with pytest.raises(ValueError):
        calcular_frete(21.0, "mesma_regiao", 100.0)


# 4) Entradas inválidas (2 casos)
def test_entrada_invalida_destino_desconhecido():
    with pytest.raises(ValueError):
        calcular_frete(5.0, "interplanetario", 100.0)


def test_entrada_invalida_valor_pedido_negativo():
    with pytest.raises(ValueError):
        calcular_frete(5.0, "mesma_regiao", -1.0)


# 5) Property-Based Testing (mínimo 3 propriedades)
@given(
    peso=st.floats(min_value=0.01, max_value=20.0, allow_nan=False, allow_infinity=False),
    destino=st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]),
    valor=st.floats(min_value=0.0, max_value=200.0, allow_nan=False, allow_infinity=False),
)
def test_propriedade_frete_nunca_negativo(peso, destino, valor):
    frete = calcular_frete(peso, destino, valor)
    assert frete >= 0.0


@given(
    peso=st.floats(min_value=0.01, max_value=20.0, allow_nan=False, allow_infinity=False),
    destino=st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]),
    valor=st.floats(min_value=200.01, max_value=10_000.0, allow_nan=False, allow_infinity=False),
)
def test_propriedade_pedido_acima_200_frete_zero(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) == 0.0


@given(
    peso=st.floats(min_value=0.01, max_value=20.0, allow_nan=False, allow_infinity=False),
    valor=st.floats(min_value=0.0, max_value=200.0, allow_nan=False, allow_infinity=False),
)
def test_propriedade_outra_regiao_maior_ou_igual_mesma(peso, valor):
    frete_mesma = calcular_frete(peso, "mesma_regiao", valor)
    frete_outra = calcular_frete(peso, "outra_regiao", valor)
    assert frete_outra >= frete_mesma
