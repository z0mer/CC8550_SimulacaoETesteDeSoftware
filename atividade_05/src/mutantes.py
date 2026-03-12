# MUTANTE 1 – subtrair: substituir - por +
def subtrair_m1(a, b):
    return a + b  # - → +

# MUTANTE 2 – subtrair: substituir - por *
def subtrair_m2(a, b):
    return a * b  # - → *

# MUTANTE 3 – eh_multiplo_de_tres: substituir == por !=
def eh_multiplo_de_tres_m3(n):
    return n % 3 != 0  # == → !=

# MUTANTE 4 – eh_multiplo_de_tres: substituir % por /
def eh_multiplo_de_tres_m4(n):
    return n / 3 == 0  # % → /

# MUTANTE 5 – menor_numero: substituir < por <=
def menor_numero_m5(a, b):
    if a <= b:  # < → <=
        return a
    else:
        return b

# MUTANTE 6 – menor_numero: substituir < por >
def menor_numero_m6(a, b):
    if a > b:  # < → >
        return a
    else:
        return b

# MUTANTE 7 – calcular_dobro_se_par: substituir == por !=
def calcular_dobro_se_par_m7(n):
    if n % 2 != 0:  # == → !=
        return n * 2
    return n

# MUTANTE 8 – calcular_dobro_se_par: substituir * por **
def calcular_dobro_se_par_m8(n):
    if n % 2 == 0:
        return n ** 2  # * → **
    return n

# MUTANTE 9 – classificar_temperatura: substituir >= por > na primeira condição
def classificar_temperatura_m9(temp):
    if temp > 30:  # >= → >
        return "Quente"
    elif temp >= 15:
        return "Agradável"
    else:
        return "Frio"

# MUTANTE 10 – classificar_temperatura: substituir >= por > na segunda condição
def classificar_temperatura_m10(temp):
    if temp >= 30:
        return "Quente"
    elif temp > 15:  # >= → >
        return "Agradável"
    else:
        return "Frio"