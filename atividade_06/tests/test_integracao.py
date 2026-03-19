import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from repositorio import HistoricoRepositorio
from calculadora import Calculadora

class TestIntegracao(unittest.TestCase):
    def setUp(self):
        self.repo = HistoricoRepositorio()
        self.calc = Calculadora(self.repo)

    # --- EXEMPLOS DO PDF ---
    def test_operacoes_sequenciais(self):
        # 2+3=5, depois 5*4=20, depois 20/2=10
        self.calc.somar(2, 3)
        self.calc.multiplicar(self.calc.obter_ultimo_resultado(), 4)
        self.calc.dividir(self.calc.obter_ultimo_resultado(), 2)

        assert self.calc.obter_ultimo_resultado() == 10
        assert self.repo.total() == 3

    def test_historico_registra_formato_correto(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        registros = self.repo.listar()
        
        assert "2 + 3 = 5" in registros
        assert "4 * 5 = 20" in registros

    def test_limpar_historico(self):
        self.calc.somar(1, 1)
        self.repo.limpar()
        assert self.repo.total() == 0

    # --- TESTE ADICIONAL EXTRA ---
    def test_historico_mantem_ordem_correta(self):
        self.calc.somar(1, 1)
        self.calc.subtrair(5, 2)
        registros = self.repo.listar()
        
        # Garante que o registo na posição 0 foi o primeiro a ser feito
        assert registros[0] == "1 + 1 = 2"
        assert registros[1] == "5 - 2 = 3"