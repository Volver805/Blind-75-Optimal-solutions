class Solution:
    def countBits(self, n: int) -> List[int]:
        @functools.lru_cache()
        def count1(b, c=0):
            if b == 0:
                return c
            return count1(b & b-1, c+1)
        res = [0]*(n+1)
        for i in range(n+1):
            res[i] = count1(i)
        return res