import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from storage import InMemoryStorage
from repository import ProdutoRepository, PedidoRepository
from service import ProdutoService, PedidoService

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"],
    storage_uri="memory://",
    headers_enabled=True,
)

_produto_storage = InMemoryStorage()
_pedido_storage = InMemoryStorage()
_produto_repo = ProdutoRepository(_produto_storage)
_pedido_repo = PedidoRepository(_pedido_storage)
_produto_service = ProdutoService(_produto_repo)
_pedido_service = PedidoService(_produto_repo, _pedido_repo)


def _seed_produtos():
    for i in range(1, 51):
        _produto_service.cadastrar_produto(
            nome=f"Produto Black Friday {i:02d}",
            preco=round(10.0 + i * 2.5, 2),
            estoque=1000,
        )


_seed_produtos()


@app.route("/saude")
def saude():
    return jsonify({"status": "ok"})


@app.route("/produtos")
@limiter.limit("100 per minute")
def listar_produtos():
    produtos = _produto_service.listar_produtos()
    return jsonify([
        {"id": p.id, "nome": p.nome, "preco": p.preco, "estoque": p.estoque}
        for p in produtos
    ])


@app.route("/produtos/<int:id>")
@limiter.limit("100 per minute")
def buscar_produto(id):
    try:
        produto = _produto_service.buscar_produto(id)
        return jsonify({"id": produto.id, "nome": produto.nome, "preco": produto.preco, "estoque": produto.estoque})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404


@app.route("/carrinho", methods=["POST"])
@limiter.limit("100 per minute")
def adicionar_carrinho():
    data = request.get_json()
    if not data or "produto_id" not in data or "quantidade" not in data:
        return jsonify({"erro": "produto_id e quantidade são obrigatórios"}), 400
    try:
        produto = _produto_service.buscar_produto(data["produto_id"])
        return jsonify({
            "mensagem": "Item adicionado ao carrinho",
            "produto_id": produto.id,
            "quantidade": data["quantidade"],
            "subtotal": round(produto.preco * data["quantidade"], 2),
        })
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404


@app.route("/pedidos", methods=["POST"])
@limiter.limit("100 per minute")
def criar_pedido():
    data = request.get_json()
    if not data or "itens" not in data:
        return jsonify({"erro": "itens é obrigatório"}), 400
    try:
        pedido = _pedido_service.criar_pedido(data["itens"])
        return jsonify({
            "id": pedido.id,
            "total": pedido.total,
            "status": pedido.status.value,
            "itens": [
                {"produto_id": i.produto_id, "quantidade": i.quantidade, "preco_unitario": i.preco_unitario}
                for i in pedido.itens
            ],
        }), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 422


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
