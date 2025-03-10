class DoubleNode:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if value is not None:  # Puedes agregar más validaciones si es necesario
            self._data = value
        else:
            raise ValueError("El dato no puede ser None")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        if isinstance(node, DoubleNode) or node is None:
            self._next = node
        else:
            raise TypeError("next debe ser una instancia de DoubleNode o None")

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        if isinstance(node, DoubleNode) or node is None:
            self._prev = node
        else:
            raise TypeError("prev debe ser una instancia de DoubleNode o None")
