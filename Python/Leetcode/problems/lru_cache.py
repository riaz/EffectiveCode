class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int ):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        
        self.remove(node)
        self.add(node)

        return node.val    
    
    def put(self, key: int, value: int) -> int:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)
    
        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]
        
    def remove(self, node):
        node.prev.next  = node.next
        node.next.prev  = node.prev

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
    