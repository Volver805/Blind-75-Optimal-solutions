class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num = maxNum = nums[0]
        for i in range(1, len(nums)):
            num = max(nums[i], num + nums[i])
            maxNum = max(maxNum, num)
        return maxNum