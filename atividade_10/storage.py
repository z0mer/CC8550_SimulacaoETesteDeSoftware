import threading
from typing import Any, Dict, Optional


class InMemoryStorage:
    def __init__(self):
        self._data: Dict[int, Any] = {}
        # Lock garante atomicidade em cenários com múltiplas threads simultâneas,
        # como nos testes de escalabilidade com ThreadPoolExecutor.
        self._lock = threading.Lock()

    def add(self, id: int, item: Any) -> None:
        with self._lock:
            self._data[id] = item

    def get(self, id: int) -> Optional[Any]:
        with self._lock:
            return self._data.get(id)

    def get_all(self) -> list:
        with self._lock:
            # Cópia defensiva: evita que o chamador itere sobre o dict
            # enquanto outra thread o modifica fora do lock.
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
