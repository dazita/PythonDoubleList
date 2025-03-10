from DoubleNode import DoubleNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        aux = DoubleNode(data)
        if self.is_empty():
            self.head = aux
            self.tail = aux
        else:
            self.tail.next = aux
            aux.prev = self.tail
            self.tail = aux

    def is_empty(self):
        return self.head is None

    def exist(self, data):
        aux = self.head
        while aux is not None:
            if aux.data == data:
                return True
            aux = aux.next
        return False

    def remove(self, data):
        aux = self.head
        while aux is not None:
            if aux.data == data:
                if self.head.data == data:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = None
                elif self.tail.data == data:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    aux.next.prev = aux.prev
                    aux.prev.next = aux.next
                return True
            aux = aux.next
        return False

    def size(self):
        counter = 0
        aux = self.head
        while aux is not None:
            aux = aux.next
            counter += 1
        return counter

    def get(self, index):
        aux = self.head
        counter = 0
        while aux is not None and counter < index:
            aux = aux.next
            counter += 1
        if aux is not None:
            return aux.data
        raise IndexError("Index out of range")

    def show(self):
        result = []
        aux = self.head
        while aux is not None:
            result.append(str(aux.data))
            aux = aux.next
        return "\n".join(result)

    def show_reversed(self):
        result = []
        aux = self.tail
        while aux is not None:
            result.append(str(aux.data))
            aux = aux.prev
        return "\n".join(result)

    def __iter__(self):
        self._current_node = None
        return self

    def __next__(self):
        if self._current_node is None:
            if self.head is None:
                raise StopIteration
            self._current_node = self.head
        else:
            self._current_node = self._current_node.next
            if self._current_node is None:
                raise StopIteration
        return self._current_node.data