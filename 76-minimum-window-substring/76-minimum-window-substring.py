class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, target = {}, {}
        left = right = 0
        leftRes, rightRes, resLen = None,None,  math.inf
        for ch in t:
            target[ch] = target.get(ch,0)+1
        foundNum, targetNum = 0, len(target.keys())
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0)+1
            if s[right] in target and window[s[right]] == target[s[right]]:
                foundNum += 1
            while targetNum == foundNum:
                if right-left+1 < resLen:
                    leftRes, rightRes = left, right
                    resLen = right-left+1
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    foundNum -= 1
                left += 1
        if resLen == math.inf:
            return ""
        return s[leftRes:rightRes+1]
