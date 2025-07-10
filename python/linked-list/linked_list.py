class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous

    def has_succeeding(self) -> bool:
        return self.succeeding != None
    
    def has_previous(self) -> bool:
        return self.previous != None
    
    def set_succeeding(self, node) -> None:
        self.succeeding = node

    def set_previous(self, node) -> None:
        self.previous = node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def _is_empty(self) -> bool:
        return self.head == None

    def __iter__(self):
        current_node = self.head
        yield(current_node)
        while current_node.has_succeeding():      
            current_node = current_node.succeeding
            yield(current_node)

    def __len__(self) -> int:

        if self._is_empty():
            return 0
        elif self.head == self.tail:
            return 1
        else:
            return sum(1 for _ in iter(self))
     
    def push(self, value: int) -> None:

        new_node = Node(value, None, None)

        if self._is_empty():
            self._add_element_on_empty_list(new_node)

        else:
            self.tail.set_succeeding(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node

    def unshift(self, value: int) -> None:

        new_node = Node(value, None, None)

        if self._is_empty():
            self._add_element_on_empty_list(new_node)

        else:
            self.head.set_previous(new_node)
            new_node.set_succeeding(self.head)
            self.head = new_node

    def _add_element_on_empty_list(self, new_node: Node) -> None:
        new_node.set_previous(None)
        new_node.set_succeeding(None)
        self.head = new_node
        self.tail = new_node

    def pop(self) -> int:

        if self._is_empty():
            raise IndexError("List is empty")
        
        value_to_remove = self.tail.value
        
        if len(self) == 1:
            self._remove_element_from_linked_list_with_one_element()

        else:
            self._remove_element_from_tail_with_more_than_one_element()

        return value_to_remove 


    def shift(self) -> int:
        
        if self._is_empty():
            raise IndexError("List is empty")
        
        value_to_remove = self.head.value

        if len(self) == 1:
            self._remove_element_from_linked_list_with_one_element()

        else:
            self._remove_element_from_head_with_more_than_one_element()

        return value_to_remove
    

    def _remove_element_from_linked_list_with_one_element(self) -> None:
        self.head.set_previous = None
        self.head.set_succeeding = None
        self.tail.set_previous = None
        self.tail.set_succeeding = None
        self.head = None
        self.tail = None

    def _remove_element_from_head_with_more_than_one_element(self) -> None:
        self.head = self.head.succeeding
        self.head.previous.set_succeeding(None)
        self.head.previous.set_previous(None)
        self.head.set_previous(None)

    def _remove_element_from_tail_with_more_than_one_element(self) -> None:
        self.tail = self.tail.previous
        self.tail.succeeding.set_previous(None)
        self.tail.succeeding.set_succeeding(None)
        self.tail.set_succeeding(None)

    def delete(self, value: int):

        if self._is_empty():
            raise ValueError("Value not found")
        
        for node in iter(self):
            if node.value == value:
                return self._remove_node(node)
                 
        raise ValueError("Value not found")
    
    def _remove_node(self, node: Node) -> int:

        value_to_remove = node.value

        if len(self) == 1:
            self._remove_element_from_linked_list_with_one_element()

        elif node == self.head:
            self._remove_element_from_head_with_more_than_one_element()
        
        elif node == self.tail:
            self._remove_element_from_tail_with_more_than_one_element()

        else:
            node.previous.set_succeeding(node.succeeding)
            node.succeeding.set_previous(node.previous)
            node.set_previous(None)
            node.set_succeeding(None)

        return value_to_remove

