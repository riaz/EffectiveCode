# This is a implementation of stack using linkedlist


class Stack:
    """
    LIFO stack implementation using a single linked list
    """
    class _Node:
        """
        Lightweight non-public class for storing of single linked list nodes
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    # stack methods
    def __init__(self):
        # Creating an empty stack
        self._head = None
        self._size = 0

    def len(self):
        """ Get the length of the stack """
        return self._size
    
    def is_empty(self):
        """ Check if the stack is empty """
        return self._size == 0

    def push(self, value):
        """ Push an element to the stack"""
        self._head = self._Node(value, self._head)
        self._size += 1

    def top(self):
        """ Getting the top of the stack """
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._head._element


    def pop(self):
        """ This is simular to top but also purges the top-node and moves the head """
        if self.is_empty():
            raise IndexError("stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    

    
