class Solution:
    def characterReplacement(self, s: str, k: int):
        left = 0
        counter = {s[0]:1}
        res = maxFreq = 1
        for right in range(1, len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            maxFreq = max(maxFreq, counter[s[right]])
            # to get the amount of characters to get replaced we will subtract the window size                   from the amount of the mos frequent number
            while (right-left+1) - maxFreq > k:
                counter[s[left]] -= 1
                left += 1
        return max(res, right-left+1) 