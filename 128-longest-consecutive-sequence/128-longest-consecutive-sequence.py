class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 in nums:
                continue
            # assume this is the start of the longest consecutive seq
            seq = 1
            curr = num
            while curr+1 in nums:
                seq += 1
                curr = curr+1
            res = max(res, seq)
        return res