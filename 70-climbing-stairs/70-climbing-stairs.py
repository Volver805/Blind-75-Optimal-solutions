class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.isEqualTarget(n)
        
    def isEqualTarget(self, target, c=0):
        if c > target:
            return 0
        if c == target:
            return 1
        if c in self.memo:
            return self.memo[c]
        res = self.isEqualTarget(target,c+1) + self.isEqualTarget(target, c+2)
        self.memo[c] = res
        return res