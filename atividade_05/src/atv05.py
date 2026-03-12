# meu_programa.py

def subtrair(a, b):
    """Retorna a subtração de b em a."""
    return a - b


def eh_multiplo_de_tres(n):
    """Retorna True se n for múltiplo de 3, False caso contrário."""
    return n % 3 == 0


def menor_numero(a, b):
    """Retorna o menor entre dois números."""
    if a < b:
        return a
    else:
        return b


def calcular_dobro_se_par(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 2 == 0:
        return n * 2
    return n


def classificar_temperatura(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "Quente"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"