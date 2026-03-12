import pytest
import sys
sys.path.insert(0, './src')
from mutantes import (
    subtrair_m1 as subtrair_1,
    subtrair_m2 as subtrair_2,
    eh_multiplo_de_tres_m3 as eh_multiplo_de_tres,
    menor_numero_m5 as menor_numero_5,
    menor_numero_m6 as menor_numero_6,
    calcular_dobro_se_par_m7 as calcular_dobro_se_par,
    classificar_temperatura_m9 as classificar_temperatura_9,
    classificar_temperatura_m10 as classificar_temperatura_10
)

def test_subtrair_mutantes():
    # Vai falhar com M1 e M2 (Mutantes Mortos)
    assert subtrair_1(10, 4) == 6
    assert subtrair_2(10, 4) == 6

def test_eh_multiplo_mutantes():
    # Vai falhar com M3 e M4 (Mutantes Mortos)
    assert eh_multiplo_de_tres(9) is True

def test_menor_numero_mutantes():
    # M5 sobrevive porque testamos com 3 e 8, e 3 <= 8 é verdade na mesma
    assert menor_numero_5(3, 8) == 3
    # M6 morre
    assert menor_numero_6(3, 8) == 3

def test_calcular_dobro_mutantes():
    # M7 morre (vai retornar 4 em vez de 8)
    assert calcular_dobro_se_par(4) == 8

def test_classificar_temperatura_mutantes():
    # M9 morre com o valor exato de 30
    assert classificar_temperatura_9(30) == "Quente"
    
    # M10 sobrevive porque nenhum teste original testa exatamente o limite de 15 graus
    assert classificar_temperatura_10(10) == "Frio"
