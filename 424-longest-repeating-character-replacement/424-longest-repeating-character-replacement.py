class Solution:
    def characterReplacement(self, s: str, k: int):
        mostFrequent = s[0]
        left = 0
        right = 1
        counter = {mostFrequent:1}
        res = 1
        while right < len(s):
            if s[right] in counter:
                counter[s[right]] += 1
                if counter[s[right]] > counter[mostFrequent]:
                    mostFrequent = s[right]
            else:
                counter[s[right]] = 1
            if sum(counter.values())-counter[mostFrequent] > k:
                res = max(res, right-left)
                counter[s[left]] -= 1
                left += 1    
            right += 1
        return max(res, right-left) 