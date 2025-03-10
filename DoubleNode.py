class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


    def get_data(self):
        return self._data

    def set_data(self, value):
        if value is not None:
            self._data = value
        else:
            raise ValueError("El dato no puede ser None")


    def get_next(self):
        return self._next

    def set_next(self, node):
        if isinstance(node, DoubleNode) or node is None:
            self._next = node
        else:
            raise TypeError("next debe ser una instancia de DoubleNode o None")

    
    def get_prev(self):
        return self._prev

    def set_prev(self, node):
        if isinstance(node, DoubleNode) or node is None:
            self._prev = node
        else:
            raise TypeError("prev debe ser una instancia de DoubleNode o None")