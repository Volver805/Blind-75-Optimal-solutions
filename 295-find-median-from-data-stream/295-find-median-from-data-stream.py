class MedianFinder:
    
    def __init__(self):
        self.lo = []
        self.loSize = 0
        self.hi = []
        self.hiSize = 0
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, num*-1)
        heapq.heappush(self.hi, heapq.heappop(self.lo) * -1)
        self.hiSize += 1
        if self.hiSize > self.loSize:
            heapq.heappush(self.lo, heapq.heappop(self.hi) * -1)
            self.loSize += 1
            self.hiSize -= 1
            
    def findMedian(self) -> float:
        if  self.loSize > self.hiSize:
            return self.lo[0]*-1
        else:
            return ((self.lo[0]*-1) + self.hi[0]) /2
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()