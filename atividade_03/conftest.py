"""Fixtures para testes de frete."""

import pytest


@pytest.fixture
def destinos_validos():
    return ["mesma_regiao", "outra_regiao", "internacional"]


@pytest.fixture
def valores_limite_peso():
    return [1.0, 5.0, 20.0]
