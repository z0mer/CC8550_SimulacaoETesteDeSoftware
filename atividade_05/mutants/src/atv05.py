# meu_programa.py

from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
def subtrair(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_subtrair__mutmut_orig, x_subtrair__mutmut_mutants, args, kwargs, None)
def x_subtrair__mutmut_orig(a, b):
    """Retorna a subtração de b em a."""
    return a - b
def x_subtrair__mutmut_1(a, b):
    """Retorna a subtração de b em a."""
    return a + b

x_subtrair__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_subtrair__mutmut_1': x_subtrair__mutmut_1
}
x_subtrair__mutmut_orig.__name__ = 'x_subtrair'


def eh_multiplo_de_tres(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_eh_multiplo_de_tres__mutmut_orig, x_eh_multiplo_de_tres__mutmut_mutants, args, kwargs, None)


def x_eh_multiplo_de_tres__mutmut_orig(n):
    """Retorna True se n for múltiplo de 3, False caso contrário."""
    return n % 3 == 0


def x_eh_multiplo_de_tres__mutmut_1(n):
    """Retorna True se n for múltiplo de 3, False caso contrário."""
    return n / 3 == 0


def x_eh_multiplo_de_tres__mutmut_2(n):
    """Retorna True se n for múltiplo de 3, False caso contrário."""
    return n % 4 == 0


def x_eh_multiplo_de_tres__mutmut_3(n):
    """Retorna True se n for múltiplo de 3, False caso contrário."""
    return n % 3 != 0


def x_eh_multiplo_de_tres__mutmut_4(n):
    """Retorna True se n for múltiplo de 3, False caso contrário."""
    return n % 3 == 1

x_eh_multiplo_de_tres__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_eh_multiplo_de_tres__mutmut_1': x_eh_multiplo_de_tres__mutmut_1, 
    'x_eh_multiplo_de_tres__mutmut_2': x_eh_multiplo_de_tres__mutmut_2, 
    'x_eh_multiplo_de_tres__mutmut_3': x_eh_multiplo_de_tres__mutmut_3, 
    'x_eh_multiplo_de_tres__mutmut_4': x_eh_multiplo_de_tres__mutmut_4
}
x_eh_multiplo_de_tres__mutmut_orig.__name__ = 'x_eh_multiplo_de_tres'


def menor_numero(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_menor_numero__mutmut_orig, x_menor_numero__mutmut_mutants, args, kwargs, None)


def x_menor_numero__mutmut_orig(a, b):
    """Retorna o menor entre dois números."""
    if a < b:
        return a
    else:
        return b


def x_menor_numero__mutmut_1(a, b):
    """Retorna o menor entre dois números."""
    if a <= b:
        return a
    else:
        return b

x_menor_numero__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_menor_numero__mutmut_1': x_menor_numero__mutmut_1
}
x_menor_numero__mutmut_orig.__name__ = 'x_menor_numero'


def calcular_dobro_se_par(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_calcular_dobro_se_par__mutmut_orig, x_calcular_dobro_se_par__mutmut_mutants, args, kwargs, None)


def x_calcular_dobro_se_par__mutmut_orig(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 2 == 0:
        return n * 2
    return n


def x_calcular_dobro_se_par__mutmut_1(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n / 2 == 0:
        return n * 2
    return n


def x_calcular_dobro_se_par__mutmut_2(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 3 == 0:
        return n * 2
    return n


def x_calcular_dobro_se_par__mutmut_3(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 2 != 0:
        return n * 2
    return n


def x_calcular_dobro_se_par__mutmut_4(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 2 == 1:
        return n * 2
    return n


def x_calcular_dobro_se_par__mutmut_5(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 2 == 0:
        return n / 2
    return n


def x_calcular_dobro_se_par__mutmut_6(n):
    """Retorna o dobro do número se ele for par, senão retorna ele mesmo."""
    if n % 2 == 0:
        return n * 3
    return n

x_calcular_dobro_se_par__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_calcular_dobro_se_par__mutmut_1': x_calcular_dobro_se_par__mutmut_1, 
    'x_calcular_dobro_se_par__mutmut_2': x_calcular_dobro_se_par__mutmut_2, 
    'x_calcular_dobro_se_par__mutmut_3': x_calcular_dobro_se_par__mutmut_3, 
    'x_calcular_dobro_se_par__mutmut_4': x_calcular_dobro_se_par__mutmut_4, 
    'x_calcular_dobro_se_par__mutmut_5': x_calcular_dobro_se_par__mutmut_5, 
    'x_calcular_dobro_se_par__mutmut_6': x_calcular_dobro_se_par__mutmut_6
}
x_calcular_dobro_se_par__mutmut_orig.__name__ = 'x_calcular_dobro_se_par'


def classificar_temperatura(temp):
    args = [temp]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_classificar_temperatura__mutmut_orig, x_classificar_temperatura__mutmut_mutants, args, kwargs, None)


def x_classificar_temperatura__mutmut_orig(temp):
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


def x_classificar_temperatura__mutmut_1(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp > 30:
        return "Quente"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_2(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 31:
        return "Quente"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_3(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "XXQuenteXX"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_4(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "quente"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_5(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "QUENTE"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_6(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "Quente"
    elif temp > 15:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_7(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "Quente"
    elif temp >= 16:
        return "Agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_8(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "Quente"
    elif temp >= 15:
        return "XXAgradávelXX"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_9(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "Quente"
    elif temp >= 15:
        return "agradável"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_10(temp):
    """Classifica a temperatura:
    >= 30: 'Quente'
    >= 15 e < 30: 'Agradável'
    < 15: 'Frio'
    """
    if temp >= 30:
        return "Quente"
    elif temp >= 15:
        return "AGRADÁVEL"
    else:
        return "Frio"


def x_classificar_temperatura__mutmut_11(temp):
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
        return "XXFrioXX"


def x_classificar_temperatura__mutmut_12(temp):
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
        return "frio"


def x_classificar_temperatura__mutmut_13(temp):
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
        return "FRIO"

x_classificar_temperatura__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_classificar_temperatura__mutmut_1': x_classificar_temperatura__mutmut_1, 
    'x_classificar_temperatura__mutmut_2': x_classificar_temperatura__mutmut_2, 
    'x_classificar_temperatura__mutmut_3': x_classificar_temperatura__mutmut_3, 
    'x_classificar_temperatura__mutmut_4': x_classificar_temperatura__mutmut_4, 
    'x_classificar_temperatura__mutmut_5': x_classificar_temperatura__mutmut_5, 
    'x_classificar_temperatura__mutmut_6': x_classificar_temperatura__mutmut_6, 
    'x_classificar_temperatura__mutmut_7': x_classificar_temperatura__mutmut_7, 
    'x_classificar_temperatura__mutmut_8': x_classificar_temperatura__mutmut_8, 
    'x_classificar_temperatura__mutmut_9': x_classificar_temperatura__mutmut_9, 
    'x_classificar_temperatura__mutmut_10': x_classificar_temperatura__mutmut_10, 
    'x_classificar_temperatura__mutmut_11': x_classificar_temperatura__mutmut_11, 
    'x_classificar_temperatura__mutmut_12': x_classificar_temperatura__mutmut_12, 
    'x_classificar_temperatura__mutmut_13': x_classificar_temperatura__mutmut_13
}
x_classificar_temperatura__mutmut_orig.__name__ = 'x_classificar_temperatura'