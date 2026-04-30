from storage import InMemoryStorage
from task import Task


class TaskRepository:
    def __init__(self, storage: InMemoryStorage = None):
        self.storage = storage if storage is not None else InMemoryStorage()
        self._next_id = 1

    def save(self, task: Task) -> Task:
        task.id = self._next_id
        self.storage.add(self._next_id, task)
        self._next_id += 1
        return task

    def find_by_id(self, id: int) -> Task:
        return self.storage.get(id)

    def find_all(self) -> list:
        return self.storage.get_all()

    def delete(self, id: int):
        self.storage.delete(id)
