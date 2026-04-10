import unittest
from estoque import Estoque

class TestEstoqueFEI(unittest.TestCase):

    def setUp(self):
        self.sistema = Estoque()

    # --- TESTE 01 ---
    # RED: Falha pois o método consultar_quantidade não existia.
    # GREEN: Criado método retornando self._itens.get(nome, 0).
    # REFACTOR: N/A.
    def test_consultar_inexistente_retorna_zero(self):
        self.assertEqual(self.sistema.consultar_quantidade("Teclado"), 0)

    # --- TESTE 02 ---
    # RED: Falha ao tentar adicionar (AttributeError).
    # GREEN: Criado adicionar_produto para inserir no dicionário.
    # REFACTOR: N/A.
    def test_adicionar_novo_produto(self):
        self.sistema.adicionar_produto("Mouse", 10)
        self.assertEqual(self.sistema.consultar_quantidade("Mouse"), 10)

    # --- TESTE 03 ---
    # RED: A implementação inicial substituía o valor em vez de somar.
    # GREEN: Alterado para usar o operador +=.
    # REFACTOR: Implementado defaultdict no __init__ para simplificar a soma.
    def test_incrementar_produto_ja_existente(self):
        self.sistema.adicionar_produto("Monitor", 2)
        self.sistema.adicionar_produto("Monitor", 3)
        self.assertEqual(self.sistema.consultar_quantidade("Monitor"), 5)

    # --- TESTE 04 ---
    # RED: O sistema aceitava quantidades negativas na adição.
    # GREEN: Adicionado 'if quantidade <= 0: raise ValueError'.
    # REFACTOR: Validação movida para o método privado _validar_quantidade.
    def test_erro_adicionar_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            self.sistema.adicionar_produto("Cabo", -5)

    # --- TESTE 05 ---
    # RED: remover_produto não existia.
    # GREEN: Criado método que subtrai do dicionário.
    # REFACTOR: N/A.
    def test_remover_produto_existente(self):
        self.sistema.adicionar_produto("Webcam", 10)
        self.sistema.remover_produto("Webcam", 4)
        self.assertEqual(self.sistema.consultar_quantidade("Webcam"), 6)

    # --- TESTE 06 ---
    # RED: O estoque ficava negativo se removesse demais.
    # GREEN: Adicionada trava de segurança comparando com consultar_quantidade.
    # REFACTOR: N/A.
    def test_erro_remover_mais_que_disponivel(self):
        self.sistema.adicionar_produto("SSD", 2)
        with self.assertRaises(ValueError):
            self.sistema.remover_produto("SSD", 5)

    # --- TESTE 07 ---
    # RED: Remoção negativa acabava somando itens ao estoque.
    # GREEN: Aplicada validação de valor positivo também na remoção.
    # REFACTOR: Reuso do método _validar_quantidade.
    def test_erro_remover_quantidade_invalida(self):
        with self.assertRaises(ValueError):
            self.sistema.remover_produto("RAM", 0)

    # --- TESTE 08 ---
    # RED: listar_produtos não existia.
    # GREEN: Criado para retornar as chaves do dicionário.
    # REFACTOR: Alterado para filtrar apenas itens com saldo > 0 (List Comprehension).
    def test_listar_produtos_ativos(self):
        self.sistema.adicionar_produto("CPU", 1)
        self.sistema.adicionar_produto("Pasta", 10)
        self.sistema.remover_produto("CPU", 1)
        lista = self.sistema.listar_produtos()
        self.assertIn("Pasta", lista)
        self.assertNotIn("CPU", lista)

    # --- TESTE 09 ---
    # RED: produto_mais_estocado não existia.
    # GREEN: Implementado usando a função built-in max().
    # REFACTOR: Otimizado o parâmetro key para buscar diretamente no dicionário.
    def test_produto_com_maior_estoque(self):
        self.sistema.adicionar_produto("A", 5)
        self.sistema.adicionar_produto("B", 20)
        self.assertEqual(self.sistema.produto_mais_estocado(), "B")

    # --- TESTE 10 ---
    # RED: max() falhava se o dicionário estivesse vazio.
    # GREEN: Adicionada verificação 'if not self._itens: return None'.
    # REFACTOR: Ajustado para verificar a lista de produtos ativos (saldo > 0).
    def test_mais_estocado_vazio_retorna_none(self):
        self.assertIsNone(self.sistema.produto_mais_estocado())

    # --- TESTES ADICIONAIS (11 a 20) ---
    
    def test_fluxo_completo_adicao_remocao(self):
        # RED/GREEN: Garante que múltiplas operações não corrompem o estado.
        self.sistema.adicionar_produto("X", 10)
        self.sistema.remover_produto("X", 3)
        self.sistema.adicionar_produto("X", 5)
        self.assertEqual(self.sistema.consultar_quantidade("X"), 12)

    def test_independencia_entre_nomes(self):
        # RED/GREEN: Garante que chaves diferentes não se misturam.
        self.sistema.adicionar_produto("Suporte", 10)
        self.sistema.adicionar_produto("Câmera", 5)
        self.assertEqual(self.sistema.consultar_quantidade("Suporte"), 10)

    def test_mais_estocado_apos_limpar_estoque(self):
        # RED/GREEN: Se todos os itens chegarem a 0, deve retornar None.
        self.sistema.adicionar_produto("A", 10)
        self.sistema.remover_produto("A", 10)
        self.assertIsNone(self.sistema.produto_mais_estocado())

    def test_remover_ate_zerar(self):
        # RED/GREEN: Valida se o sistema permite saldo exatamente zero.
        self.sistema.adicionar_produto("Fone", 1)
        self.sistema.remover_produto("Fone", 1)
        self.assertEqual(self.sistema.consultar_quantidade("Fone"), 0)

    def test_ordem_de_listagem_vazia(self):
        # RED/GREEN: Lista deve vir vazia no início.
        self.assertEqual(self.sistema.listar_produtos(), [])

    def test_grandes_quantidades(self):
        # RED/GREEN: Testa limites numéricos (stress test simples).
        self.sistema.adicionar_produto("Parafuso", 999999)
        self.assertEqual(self.sistema.consultar_quantidade("Parafuso"), 999999)

    def test_nomes_com_espacos(self):
        # RED/GREEN: Garante que strings complexas funcionam como chaves.
        nome_longo = "Cadeira Gamer Preta 2024"
        self.sistema.adicionar_produto(nome_longo, 1)
        self.assertEqual(self.sistema.consultar_quantidade(nome_longo), 1)

    def test_case_sensitivity_produtos(self):
        # RED/GREEN: Valida se diferencia 'Produto' de 'produto'.
        self.sistema.adicionar_produto("Caixa", 10)
        self.sistema.adicionar_produto("caixa", 5)
        self.assertNotEqual(self.sistema.consultar_quantidade("Caixa"), 15)

    def test_remocoes_consecutivas(self):
        # RED/GREEN: Valida consistência de múltiplas subtrações.
        self.sistema.adicionar_produto("Pilha", 10)
        self.sistema.remover_produto("Pilha", 2)
        self.sistema.remover_produto("Pilha", 2)
        self.assertEqual(self.sistema.consultar_quantidade("Pilha"), 6)

    def test_erro_remover_de_produto_nunca_cadastrado(self):
        # RED/GREEN: Tentar remover de algo que não existe (saldo 0).
        with self.assertRaises(ValueError):
            self.sistema.remover_produto("Inexistente", 1)

if __name__ == '__main__':
    unittest.main()