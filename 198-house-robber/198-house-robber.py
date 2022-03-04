class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)
        for i in reversed(range(len(nums))):
            dp[i] = nums[i] + max(dp[i+2], dp[i+3])
        return max(dp[0], dp[1])