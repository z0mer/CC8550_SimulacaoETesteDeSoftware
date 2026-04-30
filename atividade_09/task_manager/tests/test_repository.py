import pytest
from datetime import datetime, timedelta

from task import Task, Priority, Status
from repository import TaskRepository


@pytest.fixture
def mock_storage(mocker):
    return mocker.MagicMock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(storage=mock_storage)


@pytest.fixture
def tarefa():
    return Task(
        titulo="Tarefa Teste",
        descricao="Descrição de teste",
        prioridade=Priority.MEDIA,
        prazo=datetime.now() + timedelta(days=3),
    )


# Teste 1 — save atribui ID sequencial à tarefa
def test_save_atribui_id(repo, tarefa, mock_storage):
    resultado = repo.save(tarefa)
    assert resultado.id == 1


# Teste 2 — Mock: save chama storage.add com os argumentos corretos
def test_save_chama_storage_add(repo, tarefa, mock_storage):
    repo.save(tarefa)
    mock_storage.add.assert_called_once_with(1, tarefa)


# Teste 3 — Stub: find_by_id delega ao storage (configura return_value)
def test_find_by_id_delega_ao_storage(repo, tarefa, mock_storage):
    mock_storage.get.return_value = tarefa
    resultado = repo.find_by_id(1)
    assert resultado == tarefa
    mock_storage.get.assert_called_once_with(1)


# Teste 4 — Sequência: save seguido de find_by_id retorna a tarefa salva
def test_sequencia_save_e_find_by_id(repo, tarefa, mock_storage):
    mock_storage.get.return_value = tarefa
    repo.save(tarefa)
    resultado = repo.find_by_id(1)
    assert resultado.titulo == "Tarefa Teste"


# Teste 5 — Isolamento: find_all delega ao storage e retorna lista vazia
def test_find_all_retorna_lista_vazia(repo, mock_storage):
    mock_storage.get_all.return_value = []
    resultado = repo.find_all()
    assert resultado == []
    mock_storage.get_all.assert_called_once()
