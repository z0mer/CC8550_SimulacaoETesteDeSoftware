import pytest
from datetime import datetime, timedelta

from task import Task, Priority, Status


@pytest.fixture
def tarefa_valida():
    return Task(
        titulo="Estudar pytest",
        descricao="Aprender a usar fixtures e mocks",
        prioridade=Priority.ALTA,
        prazo=datetime.now() + timedelta(days=7),
    )


# Teste 1 — Estado inicial
def test_estado_inicial(tarefa_valida):
    assert tarefa_valida.status == Status.PENDENTE
    assert tarefa_valida.id is None


# Teste 2 — Título inválido
def test_titulo_invalido():
    task = Task(
        titulo="AB",
        descricao="Descrição qualquer",
        prioridade=Priority.BAIXA,
        prazo=datetime.now() + timedelta(days=1),
    )
    with pytest.raises(ValueError, match="Título deve ter pelo menos 3 caracteres"):
        task.validar()


# Teste 3 — Prazo no passado
def test_prazo_no_passado():
    task = Task(
        titulo="Tarefa Antiga",
        descricao="Descrição qualquer",
        prioridade=Priority.MEDIA,
        prazo=datetime.now() - timedelta(days=1),
    )
    with pytest.raises(ValueError, match="prazo não pode estar no passado"):
        task.validar()


# Teste 4 — Transição válida de status (PENDENTE → EM_PROGRESSO)
def test_transicao_valida(tarefa_valida):
    tarefa_valida.atualizar_status(Status.EM_PROGRESSO)
    assert tarefa_valida.status == Status.EM_PROGRESSO


# Teste 5 — Transição inválida de status (PENDENTE → CONCLUIDA, pulando EM_PROGRESSO)
def test_transicao_invalida(tarefa_valida):
    with pytest.raises(ValueError, match="Transição inválida"):
        tarefa_valida.atualizar_status(Status.CONCLUIDA)
