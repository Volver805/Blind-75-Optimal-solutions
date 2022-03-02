class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.list = {}
        self.lru = []        

    def get(self, key: int) -> int:
        if key not in self.list: return -1
        self.lru.remove(key)
        self.lru.append(key)
        return self.list[key]
    
    def put(self, key: int, value: int) -> None:
        self.list[key] = value
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
        else: 
            self.lru.append(key)
        if len(self.list) > self.size:
            self.list.pop(self.lru.pop(0))
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)