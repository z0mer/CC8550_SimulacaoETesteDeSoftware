class Estoque:
    def __init__(self):
        self._itens = {}

    def _validar_quantidade_positiva(self, quantidade: int, operacao: str):
        # Refatoração criada para aplicar o princípio DRY (Don't Repeat Yourself) 
        # nas validações de adição e remoção.
        if quantidade <= 0:
            raise ValueError(f"Não é permitido {operacao} quantidade menor ou igual a zero.")

    def consultar_quantidade(self, nome: str) -> int:
        # Retorna 0 para produto inexistente conforme a regra de negócio.
        return self._itens.get(nome, 0)

    def adicionar_produto(self, nome: str, quantidade: int):
        self._validar_quantidade_positiva(quantidade, "adicionar")
        if nome in self._itens:
            self._itens[nome] += quantidade
        else:
            self._itens[nome] = quantidade

    def remover_produto(self, nome: str, quantidade: int):
        self._validar_quantidade_positiva(quantidade, "remover")
        
        qtd_atual = self.consultar_quantidade(nome)
        if quantidade > qtd_atual:
            raise ValueError("Não é possível remover mais unidades do que o disponível.")
            
        self._itens[nome] -= quantidade
        
        # Refatoração para manter o dicionário limpo e ajudar no listar_produtos()
        if self._itens[nome] == 0:
            del self._itens[nome]

    def listar_produtos(self) -> list:
        # Lista produtos com quantidade > 0 (considerando que itens zerados foram deletados)
        return list(self._itens.keys())

    def produto_mais_estocado(self):
        # Retorna None se o estoque estiver vazio conforme regra de negócio.
        if not self._itens:
            return None
        return max(self._itens, key=self._itens.get)