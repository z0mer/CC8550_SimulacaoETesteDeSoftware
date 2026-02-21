import pytest
from cpf import validar_cpf, formatar_cpf


# Testes de validação usando parametrização
@pytest.mark.parametrize("cpf,esperado", [
    ("11144477735", True),           # CPF válido padrão
    ("00000000191", True),           # CPF válido com zeros
    ("12345678901", False),          # Dígitos verificadores errados
    ("11111111111", False),          # Todos dígitos iguais
    ("1234567890", False),           # Menos de 11 dígitos
    ("123456789012", False),         # Mais de 11 dígitos
    ("1234567890a", False),          # Com letras
])
def test_validar_cpf(cpf, esperado):
    """Testa validação de CPF com múltiplos casos."""
    # Act
    resultado = validar_cpf(cpf)
    
    # Assert
    assert resultado is esperado


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


# Testes de formatação
def test_formatar_cpf_valido():
    """Testa formatação de CPF válido."""
    # Arrange
    cpf = "11144477735"
    formato_esperado = "111.444.777-35"
    
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


# Testes com fixtures
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
