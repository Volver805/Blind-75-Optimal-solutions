class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = LinkedList(-1, -1), LinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, key, val):
        node = LinkedList(key, val)
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.cache[key] = node
        
    def moveToHead(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def popTail(self):
        x = self.tail.prev
        self.tail.prev = x.prev
        x.prev.next = self.tail
        return x
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            if self.capacity == len(self.cache):
                self.cache.pop(self.popTail().key)
            self.addNode(key, value)

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)