class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        for j in reversed(range(len(text2))):
            for i in reversed(range(len(text1))):
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1 + memo.get((i+1, j+1), 0)
                else:
                    memo[(i, j)] = max(memo.get((i+1, j), 0), memo.get((i, j+1), 0))
        return memo[(0, 0)]