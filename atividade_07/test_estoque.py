import unittest
from estoque import Estoque

class TestEstoque(unittest.TestCase):

    def setUp(self):
        self.estoque = Estoque()

    # --- Teste 1: Consultar quantidade de produto inexistente ---
    # RED: O método consultar_quantidade não existia.
    # GREEN: Criar método retornando 0 estaticamente ou usando get() no dicionário.
    # REFACTOR: Ajustado para usar dict.get(nome, 0).
    def test_consultar_produto_inexistente_retorna_zero(self):
        self.assertEqual(self.estoque.consultar_quantidade("Teclado"), 0)

    # --- Teste 2: Adicionar novo produto ---
    # RED: O método adicionar_produto não existia e o teste falharia com AttributeError.
    # GREEN: Implementação mínima criando a chave no dicionário.
    # REFACTOR: N/A na primeira iteração.
    def test_adicionar_produto_novo(self):
        self.estoque.adicionar_produto("Mouse", 15)
        self.assertEqual(self.estoque.consultar_quantidade("Mouse"), 15)

    # --- Teste 3: Adicionar produto já existente ---
    # RED: A implementação anterior sobrescreveria o valor em vez de somar.
    # GREEN: Adicionar um `if` para incrementar caso o produto já exista.
    # REFACTOR: Lógica de verificação simplificada usando o operador in.
    def test_adicionar_produto_existente_incrementa_quantidade(self):
        self.estoque.adicionar_produto("Monitor", 5)
        self.estoque.adicionar_produto("Monitor", 3)
        self.assertEqual(self.estoque.consultar_quantidade("Monitor"), 8)

    # --- Teste 4: Adicionar quantidade inválida (<= 0) ---
    # RED: O código atual permitiria adicionar valores negativos ou zerados.
    # GREEN: Adicionar um `if quantidade <= 0: raise ValueError(...)` no método.
    # REFACTOR: Extraído para o método auxiliar _validar_quantidade_positiva para evitar código duplicado futuramente.
    def test_adicionar_quantidade_invalida_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.estoque.adicionar_produto("Cabo", 0)
        with self.assertRaises(ValueError):
            self.estoque.adicionar_produto("Cabo", -5)

    # --- Teste 5: Remover produto existente ---
    # RED: O método remover_produto não existia.
    # GREEN: Implementação mínima subtraindo o valor do dicionário.
    # REFACTOR: Adicionado `del` caso a quantidade chegue a zero para manter o estado limpo.
    def test_remover_produto_existente(self):
        self.estoque.adicionar_produto("Webcam", 10)
        self.estoque.remover_produto("Webcam", 4)
        self.assertEqual(self.estoque.consultar_quantidade("Webcam"), 6)

    # --- Teste 6: Remover mais do que o disponível ---
    # RED: O código subtrairia e deixaria o estoque negativo.
    # GREEN: Adicionada checagem para lançar ValueError se a quantidade a remover for maior que o saldo.
    # REFACTOR: N/A.
    def test_remover_mais_que_disponivel_levanta_excecao(self):
        self.estoque.adicionar_produto("Filtro de Linha", 2)
        with self.assertRaises(ValueError):
            self.estoque.remover_produto("Filtro de Linha", 5)

    # --- Teste 7: Remover quantidade inválida (<= 0) ---
    # RED: O código permitiria remoção de valores negativos (que acabariam somando ao estoque).
    # GREEN: Checar e levantar erro.
    # REFACTOR: Reutilizado o método auxiliar _validar_quantidade_positiva.
    def test_remover_quantidade_invalida_levanta_excecao(self):
        self.estoque.adicionar_produto("Mesa", 5)
        with self.assertRaises(ValueError):
            self.estoque.remover_produto("Mesa", 0)

    # --- Teste 8: Listar produtos disponíveis ---
    # RED: Método listar_produtos não existia.
    # GREEN: Retornar a lista de chaves do dicionário.
    # REFACTOR: Garantir que a lista venha limpa, confiando no REFACTOR do método de remover_produto que deleta chaves zeradas.
    def test_listar_produtos_com_quantidade_positiva(self):
        self.estoque.adicionar_produto("Cadeira", 10)
        self.estoque.adicionar_produto("Luminaria", 2)
        self.estoque.remover_produto("Luminaria", 2) # Fica com 0, logo não deve ser listada
        
        lista = self.estoque.listar_produtos()
        self.assertIn("Cadeira", lista)
        self.assertNotIn("Luminaria", lista)

    # --- Teste 9: Encontrar produto mais estocado ---
    # RED: Método produto_mais_estocado não existia.
    # GREEN: Fazer um loop manual buscando a maior chave/valor.
    # REFACTOR: Uso da função built-in max() do Python, que é mais eficiente e legível.
    def test_produto_mais_estocado(self):
        self.estoque.adicionar_produto("Notebook", 5)
        self.estoque.adicionar_produto("Pendrive", 50)
        self.estoque.adicionar_produto("HD Externo", 15)
        self.assertEqual(self.estoque.produto_mais_estocado(), "Pendrive")

    # --- Teste 10: Produto mais estocado com estoque vazio ---
    # RED: A função max() atual levantaria um ValueError num dicionário vazio.
    # GREEN: Adicionar checagem de tamanho do dicionário e retornar None.
    # REFACTOR: Sintaxe pythonica `if not self._itens:`
    def test_produto_mais_estocado_em_estoque_vazio_retorna_none(self):
        self.assertIsNone(self.estoque.produto_mais_estocado())

if __name__ == '__main__':
    unittest.main()