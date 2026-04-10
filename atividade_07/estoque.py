from collections import defaultdict

class Estoque:
    def __init__(self):
        # Refactor: Uso de defaultdict para evitar erros de chave inexistente
        self._itens = defaultdict(int)

    def _validar_quantidade(self, valor: int, operacao: str):
        # Refactor: Método privado para aplicar DRY (Don't Repeat Yourself) nas validações
        if valor <= 0:
            raise ValueError(f"Quantidade para {operacao} deve ser maior que zero.")

    def consultar_quantidade(self, nome: str) -> int:
        # Green: Retorna 0 para itens não cadastrados automaticamente
        return self._itens.get(nome, 0)

    def adicionar_produto(self, nome: str, quantidade: int):
        self._validar_quantidade(quantidade, "adicionar")
        # Green: Incrementa o valor. Graças ao defaultdict, não precisa de 'if nome in self._itens'
        self._itens[nome] += quantidade

    def remover_produto(self, nome: str, quantidade: int):
        self._validar_quantidade(quantidade, "remover")
        
        if quantidade > self.consultar_quantidade(nome):
            raise ValueError("Saldo insuficiente no estoque.")
            
        self._itens[nome] -= quantidade

    def listar_produtos(self) -> list:
        # Refactor: Filtra em tempo real apenas produtos com saldo positivo
        return [item for item, qtd in self._itens.items() if qtd > 0]

    def produto_mais_estocado(self):
        # Green: Verifica se há itens antes de usar a função max()
        produtos_validos = self.listar_produtos()
        if not produtos_validos:
            return None
        return max(self._itens, key=self._itens.get)