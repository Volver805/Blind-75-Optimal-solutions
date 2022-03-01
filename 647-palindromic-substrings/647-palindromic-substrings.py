class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromsCount = 0
        for i in range(len(s)):
            palindromsCount += self.getPalindromsFromCenter(s, i, i)
            palindromsCount += self.getPalindromsFromCenter(s, i, i+1)
        return palindromsCount
        
    def getPalindromsFromCenter(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count