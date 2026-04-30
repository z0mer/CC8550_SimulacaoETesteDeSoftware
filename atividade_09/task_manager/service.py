from datetime import datetime

from task import Task, Priority, Status
from repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository = None):
        """Cria o servico com um repositorio injetavel para testes."""
        self.repository = repository if repository is not None else TaskRepository()

    def criar_tarefa(
        self,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
    ) -> Task:
        """Monta, valida e salva uma nova tarefa."""
        task = Task(titulo=titulo, descricao=descricao, prioridade=prioridade, prazo=prazo)
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> list:
        """Lista todas as tarefas existentes."""
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Task:
        """Atualiza o status de uma tarefa existente."""
        task = self.repository.find_by_id(id)
        if task is None:
            raise ValueError(f"Tarefa com id {id} não encontrada.")
        task.atualizar_status(status)
        return task
