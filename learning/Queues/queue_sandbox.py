from Node_sandbox import Node
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Queue:
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0
        
    def peek(self):
        if self.is_empty():
            print("¡No hay nada que ver aquí!")
            return None
        return self.head.get_value() if self.head else None

    def enqueue(self, value):
        if not self.has_space():
            print("¡La cola está llena!")
            return
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.set_next_node(new_node)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("¡La cola ya está vacia!")
            return None

        removed_value = self.head.get_value()
        self.head = self.head.get_next_node()
        self.size -= 1
        
        if self.is_empty():
            self.tail = None
        return removed_value