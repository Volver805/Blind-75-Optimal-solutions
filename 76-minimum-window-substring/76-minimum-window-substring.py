class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = None
        left = 0
        right = 0
        characters = {}
        for ch in t:
            characters[ch] = characters.get(ch, 0) + 1
        window = {}
        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            while self.matchTables(window, characters) and left < right:
                if not res:
                    res = s[left:right+1]
                else:
                    res = min([res, s[left:right+1]],key=len)
                window[s[left]] -= 1
                left += 1
            if self.matchTables(window, characters):
                if not res:
                    res = s[left:right+1]
                else:
                    res = min([res, s[left:right+1]],key=len)
            right += 1
        if not res:
            return ""
        return res
            
    def matchTables(self, window, target):
        for ch in target.keys():
            if  target[ch] > window.get(ch,0):
                return False
        return True