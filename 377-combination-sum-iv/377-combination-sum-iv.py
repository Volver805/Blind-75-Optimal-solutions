class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in sorted(nums):
                if i-num >= 0:
                    dp[i] += dp[i-num]
                else:
                    break
        return dp[-1]