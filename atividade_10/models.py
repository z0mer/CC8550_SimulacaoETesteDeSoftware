from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


class StatusPedido(Enum):
    AGUARDANDO = "AGUARDANDO"
    CONFIRMADO = "CONFIRMADO"
    CANCELADO = "CANCELADO"


@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int
    id: Optional[int] = None

    def validar(self):
        if len(self.nome) < 3:
            raise ValueError("Nome do produto deve ter pelo menos 3 caracteres")
        if self.preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
        if self.estoque < 0:
            raise ValueError("Estoque não pode ser negativo")


@dataclass
class ItemCarrinho:
    produto_id: int
    quantidade: int
    preco_unitario: float


@dataclass
class Pedido:
    itens: List[ItemCarrinho]
    total: float
    id: Optional[int] = None
    status: StatusPedido = field(default_factory=lambda: StatusPedido.AGUARDANDO)
