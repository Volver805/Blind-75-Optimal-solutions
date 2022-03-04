class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        previous, current = [0]*(len(text1)+1), [0]*(len(text1)+1)
        
        for j in reversed(range(len(text2))):
            for i in reversed(range(len(text1))):
                if text1[i] == text2[j]:
                    current[i] = 1+previous[i+1]
                else:
                    current[i] = max(current[i+1], previous[i])
            current, previous = previous, current
        return previous[0]