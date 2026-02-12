"""
Testes para o Sistema de Validação de CPF

Contém testes parametrizados, fixtures e testes de exceção.
Segue o padrão AAA (Arrange, Act, Assert).
"""
import pytest
from cpf import validar_cpf, formatar_cpf


# Testes usando fixtures e parametrização
@pytest.mark.parametrize("cpf", [
    "11144477735",
    "00000000191",
    "52998224725",
    "111.444.777-35",
])
def test_validar_cpf_validos(cpf):
    """Testa validação de CPFs válidos usando parametrização."""
    # Arrange - cpf já vem como parâmetro
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is True


@pytest.mark.parametrize("cpf", [
    "12345678901",  # Dígitos verificadores errados
    "111.111.111-11",  # Todos dígitos iguais
    "11111111111",  # Todos dígitos iguais
    "00000000000",  # Todos zeros
    "1234567890",  # Menos de 11 dígitos
    "123456789012",  # Mais de 11 dígitos
    "1234567890a",  # Com letras
    "abc.def.ghi-jk",  # Apenas letras
])
def test_validar_cpf_invalidos(cpf):
    """Testa validação de CPFs inválidos usando parametrização."""
    # Arrange - cpf já vem como parâmetro
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_validar_cpf_string_vazia():
    """Testa CPF com string vazia."""
    # Arrange
    cpf = ""
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_validar_cpf_none():
    """Testa CPF None."""
    # Arrange
    cpf = None
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_validar_cpf_com_zeros():
    """Testa CPF válido com zeros."""
    # Arrange
    cpf = "00000000191"
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is True


def test_validar_cpf_todos_digitos_iguais():
    """Testa CPF com todos dígitos iguais (111.111.111-11)."""
    # Arrange
    cpf = "11111111111"
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_validar_cpf_menos_11_digitos():
    """Testa CPF com menos de 11 dígitos."""
    # Arrange
    cpf = "1234567890"
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_validar_cpf_mais_11_digitos():
    """Testa CPF com mais de 11 dígitos."""
    # Arrange
    cpf = "123456789012"
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_validar_cpf_com_letras():
    """Testa CPF com letras."""
    # Arrange
    cpf = "1234567890a"
    
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is False


def test_formatar_cpf_valido():
    """Testa formatação de CPF válido."""
    # Arrange
    cpf = "11144477735"
    formato_esperado = "111.444.777-35"
    
    # Act
    resultado = formatar_cpf(cpf)
    
    # Assert
    assert resultado == formato_esperado


def test_formatar_cpf_valido_com_zeros():
    """Testa formatação de CPF válido com zeros."""
    # Arrange
    cpf = "00000000191"
    formato_esperado = "000.000.001-91"
    
    # Act
    resultado = formatar_cpf(cpf)
    
    # Assert
    assert resultado == formato_esperado


def test_formatar_cpf_invalido_levanta_excecao():
    """Testa que formatar_cpf levanta ValueError para CPF inválido."""
    # Arrange
    cpf = "12345678901"
    
    # Act & Assert
    with pytest.raises(ValueError) as exc:
        formatar_cpf(cpf)
    
    assert "CPF inválido" in str(exc.value)


def test_formatar_cpf_string_vazia_levanta_excecao():
    """Testa que formatar_cpf levanta ValueError para string vazia."""
    # Arrange
    cpf = ""
    
    # Act & Assert
    with pytest.raises(ValueError) as exc:
        formatar_cpf(cpf)
    
    assert "CPF inválido" in str(exc.value)


def test_formatar_cpf_com_letras_levanta_excecao():
    """Testa que formatar_cpf levanta ValueError para CPF com letras."""
    # Arrange
    cpf = "abc.def.ghi-jk"
    
    # Act & Assert
    with pytest.raises(ValueError):
        formatar_cpf(cpf)


# Testes usando fixtures
def test_validar_cpfs_validos_com_fixture(cpfs_validos):
    """Testa múltiplos CPFs válidos usando fixture."""
    # Arrange - cpfs_validos vem da fixture
    
    # Act & Assert
    for cpf in cpfs_validos:
        resultado = validar_cpf(cpf)
        assert resultado is True, f"CPF {cpf} deveria ser válido"


def test_validar_cpfs_invalidos_com_fixture(cpfs_invalidos):
    """Testa múltiplos CPFs inválidos usando fixture."""
    # Arrange - cpfs_invalidos vem da fixture
    
    # Act & Assert
    for cpf in cpfs_invalidos:
        resultado = validar_cpf(cpf)
        assert resultado is False, f"CPF {cpf} deveria ser inválido"
