import time
from typing import Optional
from models import Produto, ItemCarrinho, Pedido
from repository import ProdutoRepository, PedidoRepository


class ProdutoService:
    def __init__(self, repository: ProdutoRepository = None):
        self.repository = repository or ProdutoRepository()

    def cadastrar_produto(self, nome: str, preco: float, estoque: int) -> Produto:
        produto = Produto(nome=nome, preco=preco, estoque=estoque)
        produto.validar()
        return self.repository.save(produto)

    def listar_produtos(self) -> list:
        time.sleep(0.001)  # simula latência de I/O de banco de dados
        return self.repository.find_all()

    def buscar_produto(self, id: int) -> Optional[Produto]:
        time.sleep(0.001)
        produto = self.repository.find_by_id(id)
        if produto is None:
            raise ValueError(f"Produto com id {id} não encontrado")
        return produto

    def atualizar_estoque(self, id: int, quantidade: int) -> Produto:
        produto = self.repository.find_by_id(id)
        if produto is None:
            raise ValueError(f"Produto com id {id} não encontrado")
        if produto.estoque < quantidade:
            raise ValueError(f"Estoque insuficiente para o produto {id}")
        produto.estoque -= quantidade
        return self.repository.save(produto)


class PedidoService:
    def __init__(
        self,
        produto_repo: ProdutoRepository = None,
        pedido_repo: PedidoRepository = None,
    ):
        self.produto_repo = produto_repo or ProdutoRepository()
        self.pedido_repo = pedido_repo or PedidoRepository()

    def criar_pedido(self, itens: list) -> Pedido:
        """
        itens: lista de dicts com chaves produto_id e quantidade
        """
        time.sleep(0.001)  # simula latência de transação no banco
        itens_pedido = []
        total = 0.0

        for item in itens:
            produto_id = item["produto_id"]
            quantidade = item["quantidade"]

            produto = self.produto_repo.find_by_id(produto_id)
            if produto is None:
                raise ValueError(f"Produto {produto_id} não encontrado")
            if produto.estoque < quantidade:
                raise ValueError(f"Estoque insuficiente para produto {produto_id}")

            item_carrinho = ItemCarrinho(
                produto_id=produto_id,
                quantidade=quantidade,
                preco_unitario=produto.preco,
            )
            itens_pedido.append(item_carrinho)
            total += produto.preco * quantidade

        pedido = Pedido(itens=itens_pedido, total=round(total, 2))
        return self.pedido_repo.save(pedido)
