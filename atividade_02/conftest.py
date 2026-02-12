"""
Fixtures para testes de CPF

Contém fixtures compartilhadas entre os testes.
"""
import pytest


@pytest.fixture
def cpfs_validos():
    """Lista de CPFs válidos para testes."""
    return [
        "11144477735",  # CPF válido padrão
        "00000000191",  # CPF válido com zeros
        "52998224725",  # CPF válido
        "111.444.777-35",  # CPF válido formatado
    ]


@pytest.fixture
def cpfs_invalidos():
    """Lista de CPFs inválidos para testes."""
    return [
        "12345678901",  # Dígitos verificadores errados
        "111.111.111-11",  # Todos dígitos iguais
        "11111111111",  # Todos dígitos iguais sem formatação
        "1234567890",  # Menos de 11 dígitos
        "123456789012",  # Mais de 11 dígitos
        "1234567890a",  # Com letras
        "abc.def.ghi-jk",  # Apenas letras
        "",  # String vazia
        "123",  # Muito curto
    ]
