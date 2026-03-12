# test_meu_programa.py
import pytest
import sys
sys.path.insert(0, './src')
from atv05 import (
    subtrair, 
    eh_multiplo_de_tres, 
    menor_numero, 
    calcular_dobro_se_par, 
    classificar_temperatura
)

def test_subtrair_positivos():
    assert subtrair(10, 4) == 6

def test_subtrair_negativos():
    assert subtrair(-5, -2) == -3

def test_eh_multiplo_de_tres_verdadeiro():
    assert eh_multiplo_de_tres(9) is True

def test_eh_multiplo_de_tres_falso():
    assert eh_multiplo_de_tres(10) is False

def test_menor_numero_primeiro_menor():
    assert menor_numero(3, 8) == 3

def test_menor_numero_segundo_menor():
    assert menor_numero(10, 4) == 4

def test_calcular_dobro_se_par_com_par():
    assert calcular_dobro_se_par(4) == 8

def test_calcular_dobro_se_par_com_impar():
    assert calcular_dobro_se_par(5) == 5

def test_classificar_temperatura_quente():
    assert classificar_temperatura(30) == "Quente"

def test_classificar_temperatura_frio():
    assert classificar_temperatura(10) == "Frio"