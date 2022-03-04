from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        @lru_cache(maxsize=None)
        def lcs(i, j):
            if i == len(text1) or j == len(text2): return 0
            
            if text1[i] == text2[j]: return 1 + lcs(i+1, j+1)
            return max(lcs(i+1, j), lcs(i, j+1))
        return lcs(0, 0)