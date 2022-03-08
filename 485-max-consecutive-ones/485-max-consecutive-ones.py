class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0
        for num in nums:
            if num == 0:
                maxCount = max(maxCount, count)
                count = 0
            else:
                count += 1
        return max(maxCount, count)