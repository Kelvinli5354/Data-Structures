"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

<<<<<<< HEAD
        return self
=======
  def contains(self, value):
    pass
>>>>>>> 009b2189bcd2902a3392c78c3c876c416c8f8f5f

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.next_node:
            head = self.head
            self.head = None
            self.tail = None
            return head.value
        else:
            value = self.head.get_value()
            self.head = self.head.next_node
            return value

    def contains(self,value):
        if not self.head:
            return None
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.get_next()
        return max_value
