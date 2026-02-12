"""
Sistema de Validação de CPF

Implementação de funções para validar e formatar CPFs brasileiros.
"""


def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro.
    
    Args:
        cpf: String contendo o CPF (pode estar formatado ou não)
        
    Returns:
        True se o CPF é válido, False caso contrário
        
    Exemplos:
        >>> validar_cpf("123.456.789-01")
        False
        >>> validar_cpf("12345678901")
        False
    """
    if cpf is None:
        return False
    
    # Remove caracteres não numéricos
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    
    # Valida formato (11 dígitos)
    if len(cpf_limpo) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf_limpo == cpf_limpo[0] * 11:
        return False
    
    # Valida dígitos verificadores
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)
    
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf_limpo[9]) != digito1:
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf_limpo[i]) * (11 - i)
    
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    if int(cpf_limpo[10]) != digito2:
        return False
    
    return True


def formatar_cpf(cpf: str) -> str:
    """
    Formata um CPF no padrão XXX.XXX.XXX-XX.
    
    Args:
        cpf: String contendo o CPF sem formatação
        
    Returns:
        CPF formatado no padrão XXX.XXX.XXX-XX
        
    Raises:
        ValueError: Se o CPF for inválido
        
    Exemplos:
        >>> formatar_cpf("12345678901")
        "123.456.789-01"
    """
    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")
    
    # Remove caracteres não numéricos
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    
    # Formata o CPF
    return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
