from storage import InMemoryStorage
from task import Task


class TaskRepository:
    def __init__(self, storage: InMemoryStorage = None):
        """Cria o repositorio usando um storage injetavel para facilitar testes."""
        self.storage = storage if storage is not None else InMemoryStorage()
        self._next_id = 1

    def save(self, task: Task) -> Task:
        """Atribui um id novo, persiste a tarefa e devolve o objeto salvo."""
        task.id = self._next_id
        self.storage.add(self._next_id, task)
        self._next_id += 1
        return task

    def find_by_id(self, id: int) -> Task:
        """Busca uma tarefa pelo id."""
        return self.storage.get(id)

    def find_all(self) -> list:
        """Retorna todas as tarefas cadastradas."""
        return self.storage.get_all()

    def delete(self, id: int):
        """Remove a tarefa correspondente ao id informado."""
        self.storage.delete(id)
