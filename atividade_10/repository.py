from typing import Optional
from models import Produto, Pedido
from storage import InMemoryStorage


class ProdutoRepository:
    def __init__(self, storage: InMemoryStorage = None):
        self.storage = storage or InMemoryStorage()
        self._next_id = 1

    def save(self, produto: Produto) -> Produto:
        if produto.id is None:
            produto.id = self._next_id
            self._next_id += 1
        self.storage.add(produto.id, produto)
        return produto

    def find_by_id(self, id: int) -> Optional[Produto]:
        return self.storage.get(id)

    def find_all(self) -> list:
        return self.storage.get_all()

    def delete(self, id: int) -> bool:
        return self.storage.delete(id)


class PedidoRepository:
    def __init__(self, storage: InMemoryStorage = None):
        self.storage = storage or InMemoryStorage()
        self._next_id = 1

    def save(self, pedido: Pedido) -> Pedido:
        if pedido.id is None:
            pedido.id = self._next_id
            self._next_id += 1
        self.storage.add(pedido.id, pedido)
        return pedido

    def find_by_id(self, id: int) -> Optional[Pedido]:
        return self.storage.get(id)

    def find_all(self) -> list:
        return self.storage.get_all()
