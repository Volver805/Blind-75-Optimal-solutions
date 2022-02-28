class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, left, right = 0, None, None
        for i in range(len(s)):
            palindrome = max(self.getLongestPalindromeFromCenter(s, i, i+1), self.getLongestPalindromeFromCenter(s, i, i))
            if palindrome > res:
                res = palindrome
                left = i - (palindrome-1)//2
                right = i + palindrome//2
        return s[left:right+1]
                
            
    def getLongestPalindromeFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1