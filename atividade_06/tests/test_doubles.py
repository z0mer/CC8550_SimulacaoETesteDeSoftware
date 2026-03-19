import unittest
from unittest.mock import MagicMock
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from calculadora import Calculadora

class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    # --- EXEMPLOS DO PDF ---
    def test_soma_stub_repositorio(self):
        # stub: salvar() nao faz nada de verdade
        resultado = self.calc.somar(10, 5)
        assert resultado == 15

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        # A calculadora pode ser testada mesmo antes do repositorio existir
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        assert resultado == 21

    # --- TESTE ADICIONAL EXTRA ---
    def test_subtrair_stub_repositorio(self):
        resultado = self.calc.subtrair(20, 5)
        assert resultado == 15


class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    # --- EXEMPLOS DO PDF ---
    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        # Verifica que salvar() foi chamado exatamente uma vez
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto(self):
        self.calc.somar(4, 6)
        # Verifica o argumento exato passado ao repositorio
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        # Se houve excecao, o repositorio NAO deve ter sido acionado
        self.mock_repo.salvar.assert_not_called()
        
    # --- IMPLEMENTAÇÕES PEDIDAS ---
    def test_mock_verifica_argumento_potencia(self):
        self.calc.potencia(2, 3)
        # Usado para detetar o BUG intencional que faltava o "**"
        self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")

    # --- TESTE ADICIONAL EXTRA ---
    def test_mock_verifica_argumento_divisao(self):
        self.calc.dividir(10, 2)
        self.mock_repo.salvar.assert_called_once_with("10 / 2 = 5.0")