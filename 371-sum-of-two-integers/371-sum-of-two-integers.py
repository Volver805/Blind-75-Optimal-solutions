class Solution:
    def getSum(self, x: int, y: int) -> int:
        a, b = abs(x), abs(y)
        if a < b:
            return self.getSum(y, x)
        sign = 1 if x > 0 else -1
        if x * y >= 0:
            while b != 0:
                a,b = a^b,(a & b)<<1
        else:
            while b != 0:
                a, b = a^b, ((~a) & b) << 1
        return a*sign