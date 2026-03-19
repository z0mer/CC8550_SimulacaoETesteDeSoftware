import unittest
import sys
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from calculadora import Calculadora

class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock() # stub do repositorio
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_soma_retorna_valor_correto(self):
        resultado = self.calc.somar(5, 3)
        assert resultado == 8

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        assert self.calc.obter_ultimo_resultado() == 8

    # --- IMPLEMENTAÇÕES PEDIDAS ---
    def test_subtrair_casos(self):
        assert self.calc.subtrair(10, 4) == 6
        assert self.calc.subtrair(-5, -2) == -3

    def test_multiplicar_casos(self):
        assert self.calc.multiplicar(4, 5) == 20
        assert self.calc.multiplicar(-2, 3) == -6

    def test_dividir_casos(self):
        assert self.calc.dividir(10, 2) == 5.0
        assert self.calc.dividir(9, 4) == 2.25

    def test_potencia_casos(self):
        assert self.calc.potencia(2, 3) == 8
        assert self.calc.potencia(5, 0) == 1

    # --- TESTE ADICIONAL EXTRA ---
    def test_subtrair_atualiza_ultimo_resultado(self):
        self.calc.subtrair(10, 5)
        assert self.calc.obter_ultimo_resultado() == 5


class TestTipagem(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_tipagem_string_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_tipagem_none_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

    # --- IMPLEMENTAÇÕES PEDIDAS ---
    def test_tipagem_booleana(self):
        # O comportamento é esperado pois bool herda de int em Python
        assert self.calc.somar(True, False) == 1

    def test_tipagem_string_rejeitada_subtrair(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(10, "2")

    def test_tipagem_string_rejeitada_multiplicar(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar("4", 5)

    def test_tipagem_string_rejeitada_potencia(self):
        with self.assertRaises(TypeError):
            self.calc.potencia(2, "3")

    # --- TESTE ADICIONAL EXTRA ---
    def test_tipagem_lista_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.somar([1, 2], 3)


class TestLimiteInferiorESuperior(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_limite_zero(self):
        assert self.calc.somar(0, 5) == 5

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        assert resultado != float('inf') # nao deve transbordar

    # --- IMPLEMENTAÇÕES PEDIDAS ---
    def test_limite_divisor_muito_pequeno(self):
        assert self.calc.dividir(1, 1e-10) == 1e10

    def test_limite_expoente_negativo(self):
        assert self.calc.potencia(2, -2) == 0.25

    def test_limite_expoente_fracionario(self):
        assert self.calc.potencia(9, 0.5) == 3.0

    # --- TESTE ADICIONAL EXTRA ---
    def test_limite_base_zero_expoente_zero(self):
        # Em python 0**0 é 1
        assert self.calc.potencia(0, 0) == 1


class TestValoresForaDoIntervalo(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    # --- TESTE ADICIONAL EXTRA ---
    def test_divisao_zero_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(0, 0)


class TestMensagensDeErro(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero nao permitida"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)

    # --- TESTE ADICIONAL EXTRA ---
    def test_mensagem_tipo_invalido_potencia(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.potencia(2, "x")


class TestFluxosDeControle(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_caminho_divisao_normal(self):
        assert self.calc.dividir(10, 2) == 5.0

    def test_caminho_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    # --- TESTE ADICIONAL EXTRA ---
    def test_caminho_tipagem_erro(self):
        with self.assertRaises(TypeError):
            self.calc.somar(10, "5")