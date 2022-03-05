class Solution:
    def reverseBits(self, n: int) -> int:
        res, digit = 0, 31
        while n:
            res += (n & 1) << digit
            n >>= 1
            digit -= 1
        return res