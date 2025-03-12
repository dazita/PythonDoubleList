from DoubleNode import DoubleNode

class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    # Getter para head
    def get_head(self):
        return self.__head

    # Setter para head
    def set_head(self, node):
        self.__head = node

    # Getter para tail
    def get_tail(self):
        return self.__tail

    # Setter para tail
    def set_tail(self, node):
        self.__tail = node

    def insert(self, data):
        aux = DoubleNode(data)
        if self.is_empty():
            self.__head = aux
            self.__tail = aux
        else:
            self.__tail.set_next(aux)
            aux.set_prev(self.__tail)
            self.__tail = aux

    def is_empty(self):
        return self.__head is None

    def exist(self, data):
        aux = self.__head
        while aux is not None:
            if aux.get_data() == data:
                return True
            aux = aux.get_next()
        return False

    def remove(self, data):
        aux = self.__head
        while aux is not None:
            if aux.get_data() == data:
                if self.__head.get_data() == data:
                    if self.__head == self.__tail:
                        self.__head = None
                        self.__tail = None
                    else:
                        self.__head = self.__head.get_next()
                        self.__head.set_prev(None)
                elif self.__tail.get_data() == data:
                    self.__tail = self.__tail.get_prev()
                    self.__tail.set_next(None)
                else:
                    aux.get_next().set_prev(aux.get_prev())
                    aux.get_prev().set_next(aux.get_next())
                return True
            aux = aux.get_next()
        return False

    def size(self):
        counter = 0
        aux = self.__head
        while aux is not None:
            aux = aux.get_next()
            counter += 1
        return counter

    def get(self, index):
        aux = self.__head
        counter = 0
        while aux is not None and counter < index:
            aux = aux.get_next()
            counter += 1
        if aux is not None:
            return aux.get_data()
        raise IndexError("Index out of range")

    def show(self):
        result = []
        aux = self.__head
        while aux is not None:
            result.append(str(aux.get_data()))
            aux = aux.get_next()
        return "\n".join(result)

    def show_reversed(self):
        result = []
        aux = self.__tail
        while aux is not None:
            result.append(str(aux.get_data()))
            aux = aux.get_prev()
        return "\n".join(result)

    def __iter__(self):
        self._current_node = None
        return self

    def __next__(self):
        if self._current_node is None:
            if self.__head is None:
                raise StopIteration
            self._current_node = self.__head
        else:
            self._current_node = self._current_node.get_next()
            if self._current_node is None:
                raise StopIteration
        return self._current_node.get_data()
