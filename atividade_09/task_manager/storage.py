class InMemoryStorage:
    def __init__(self):
        """Inicializa um armazenamento simples em memoria."""
        self._data = {}

    def add(self, id, item):
        """Guarda um item associado a um id."""
        self._data[id] = item

    def get(self, id):
        """Retorna o item associado ao id, ou None se nao existir."""
        return self._data.get(id)

    def get_all(self):
        """Retorna todos os itens armazenados."""
        return list(self._data.values())

    def delete(self, id):
        """Remove o item do id, se ele existir."""
        self._data.pop(id, None)

    def clear(self):
        """Remove todos os itens do armazenamento."""
        self._data.clear()
