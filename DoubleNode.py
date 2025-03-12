class DoubleNode:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    
    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev


    def set_data(self, data):
        self.__data = data

    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node
