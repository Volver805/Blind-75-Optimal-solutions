from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def match(i=0, word= None):
            if not word:
                if i == len(s):
                    return True
                for w in wordDict:
                    if w[0] == s[i]:
                        if match(i, w):
                            return True
            elif i == len(s):
                return False
            elif word[0] == s[i]:
                return match(i+1, word[1:])
            return False
        return match()