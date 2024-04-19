from algo.linkedlist.node import Node

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the indexth node in the linked list. If the index is invalid, return -1.
        """
        if self.head:
            tmp = self.head
            count = 0
            
            while tmp:
                if index == count:
                    return tmp.val
                tmp = tmp.next
                count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
        if not self.tail: # i.e tail is empty
            self.tail = self.head
        
        self._size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.
        """
        newNode = Node(val)
        if not self.tail:
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode    
        
        self._size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list. 
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self._size:
            return  # the index is out of range for insertion
        elif index == self._size:
            self.addAtTail(val)
        else:
            count = 0
            tmp = self.head
            prev = None
            while count < index:
                count += 1
                prev = tmp
                tmp = tmp.next
            
            newNode = Node(val)

            prev.next = newNode
            newNode.next = tmp
            
            self._size += 1 # increment the size
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the indexth node in the linked list, if the index is valid.
        """
        if index > self._size:
            return  # the index is out of range for insertion
        else:
            count = 0
            tmp = self.head
            prev = None
            while count < index:
                count += 1
                prev = tmp
                tmp = tmp.next
            
            if not prev:
                # move head
                # when its the only element in the array
                # get back normal
                self.head = self.head.next                
            else:
                if tmp and tmp.next: # if not tail
                    prev.next = tmp.next
                else:
                    prev.next = None
                    self.tail = prev                              
            self._size -= 1 # increment the size
        