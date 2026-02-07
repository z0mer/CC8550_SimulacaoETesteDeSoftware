import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "source"))

from sistemaDeNotas import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas
)

class TestValidarNota:
    def test_nota_valida_inteira(self):
        assert validar_nota(0) == True
        assert validar_nota(5) == True
        assert validar_nota(10) == True
    
    def test_nota_invalida_negativa(self):
        assert validar_nota(-1) == False
    
    def test_nota_invalida_acima(self):
        assert validar_nota(11) == False
    
    def test_nota_com_decimal(self):
        # testa se aceita valores quebrados
        assert validar_nota(7.5) == True
        assert validar_nota(9.99) == True
        assert validar_nota(10.0) == True
        assert validar_nota(10.1) == False

class TestCalcularMedia:
    
    def test_media_simples(self):
        notas = [5, 7, 9]
        assert calcular_media(notas) == 7.0
    
    def test_uma_unica_nota(self):
        assert calcular_media([8.5]) == 8.5
    
    def test_media_com_decimais(self):
        notas = [6.5, 7.5, 8.0]
        resultado = calcular_media(notas)
        assert resultado == 7.333333333333333
    
    def test_ignora_notas_invalidas(self):
        notas = [5, 10, -1, 15, 7]
        resultado = calcular_media(notas)
        assert resultado == 7.333333333333333
    
    def test_lista_vazia_levanta_erro(self):
        with pytest.raises(ValueError):
            calcular_media([])
    
    def test_somente_invalidas_levanta_erro(self):
        notas = [-5, 15, 20]
        with pytest.raises(ValueError):
            calcular_media(notas)

class TestObterSituacao:
    
    def test_aprovado_nota_7(self):
        assert obter_situacao(7.0) == "Aprovado"
    
    def test_recuperacao_nota_5(self):
        assert obter_situacao(5.0) == "Recuperacao"
    
    def test_recuperacao_nota_intermediaria(self):
        assert obter_situacao(6.0) == "Recuperacao"
        assert obter_situacao(6.9) == "Recuperacao"
    
    def test_reprovado_abaixo_5(self):
        assert obter_situacao(4.9) == "Reprovado"
        assert obter_situacao(2.0) == "Reprovado"
    
    def test_media_invalida(self):
        with pytest.raises(ValueError):
            obter_situacao(-1)
        with pytest.raises(ValueError):
            obter_situacao(11)

class TestCalcularEstatisticas:
    
    def test_estatisticas_basicas(self):
        notas = [3, 5, 7, 9]
        resultado = calcular_estatisticas(notas)
        
        assert resultado["media"] == 6.0
        assert resultado["maior"] == 9
        assert resultado["menor"] == 3
    
    def test_contagem_situacoes(self):
        notas = [3, 5, 7, 9]
        resultado = calcular_estatisticas(notas)
        
        assert resultado["aprovados"] == 2
        assert resultado["recuperacao"] == 1
        assert resultado["reprovados"] == 1
    
    def test_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_estatisticas([])
    
    def test_ignora_notas_invalidas_nas_estatisticas(self):
        notas = [5, 10, -2, 12, 8]
        stats = calcular_estatisticas(notas)
        
        assert stats["maior"] == 10
        assert stats["menor"] == 5
    
    def test_somente_notas_invalidas(self):
        notas = [-5, 15, 20]
        with pytest.raises(ValueError):
            calcular_estatisticas(notas)

class TestNormalizarNotas:
    
    def test_normalizar_de_20_para_10(self):
        notas = [10, 20]
        resultado = normalizar_notas(notas, 20)
        assert resultado == [5.0, 10.0]
    
    def test_normalizar_de_100_para_10(self):
        notas = [50, 75, 100]
        resultado = normalizar_notas(notas, 100)
        assert resultado == [5.0, 7.5, 10.0]
    
    def test_normalizar_sem_parametro_nota_maxima(self):
        notas = [5, 10]
        assert normalizar_notas(notas) == [5.0, 10.0]
    
    def test_normalizar_lista_vazia(self):
        with pytest.raises(ValueError):
            normalizar_notas([])
    
    def test_nota_maxima_invalida(self):
        with pytest.raises(ValueError):
            normalizar_notas([5, 10], -10)
        with pytest.raises(ValueError):
            normalizar_notas([5, 10], 0)