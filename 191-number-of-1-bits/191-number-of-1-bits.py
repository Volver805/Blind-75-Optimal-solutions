class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n != 0:
            c += 1
            n &= (n-1) # Flip LSB
        return c