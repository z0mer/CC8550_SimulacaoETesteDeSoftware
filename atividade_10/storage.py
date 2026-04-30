import threading
from typing import Any, Dict, Optional


class InMemoryStorage:
    def __init__(self):
        self._data: Dict[int, Any] = {}
        self._lock = threading.Lock()

    def add(self, id: int, item: Any) -> None:
        with self._lock:
            self._data[id] = item

    def get(self, id: int) -> Optional[Any]:
        with self._lock:
            return self._data.get(id)

    def get_all(self) -> list:
        with self._lock:
            return list(self._data.values())

    def delete(self, id: int) -> bool:
        with self._lock:
            if id in self._data:
                del self._data[id]
                return True
            return False

    def clear(self) -> None:
        with self._lock:
            self._data.clear()
