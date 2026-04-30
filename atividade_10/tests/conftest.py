import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from storage import InMemoryStorage
from repository import ProdutoRepository, PedidoRepository
from service import ProdutoService, PedidoService
from app import app as flask_app


@pytest.fixture
def storage():
    return InMemoryStorage()


@pytest.fixture
def produto_repo(storage):
    return ProdutoRepository(storage)


@pytest.fixture
def produto_service(produto_repo):
    return ProdutoService(produto_repo)


@pytest.fixture
def pedido_repo():
    return PedidoRepository(InMemoryStorage())


@pytest.fixture
def pedido_service(produto_repo, pedido_repo):
    return PedidoService(produto_repo, pedido_repo)


@pytest.fixture
def produto_populado(produto_service):
    return produto_service.cadastrar_produto("Smart TV 4K", 3500.00, 100)


@pytest.fixture
def flask_client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client
