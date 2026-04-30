class InMemoryStorage:
    def __init__(self):
        self._data = {}

    def add(self, id, item):
        self._data[id] = item

    def get(self, id):
        return self._data.get(id)

    def get_all(self):
        return list(self._data.values())

    def delete(self, id):
        self._data.pop(id, None)

    def clear(self):
        self._data.clear()
