class Node:
    def __init__(self, value_int, next_node=None):
        self._value_int = value_int
        self._next_node = next_node

    def value(self):
        return self._value_int

    def next(self):
        return self._next_node


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._count = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self._count

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._count += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        
        value = self._head.value()
        self._head = self._head.next()
        self._count -= 1
        return value
        
    def reversed(self):
        return LinkedList(self)

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()

class EmptyListException(Exception):
    
    def __init__(self, message):
        self.message = message
