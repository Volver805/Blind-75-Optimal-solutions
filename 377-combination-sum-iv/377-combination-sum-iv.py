class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Top down solution
        dp = {}
        def getCombinations(target):
            if target == 0:
                return 1
            res = 0
            for num in nums:
                newTarget = target-num
                if newTarget in dp:
                    res += dp[newTarget]
                elif newTarget >= 0:
                    res += getCombinations(newTarget)
            dp[target] = res
            return res
        return getCombinations(target)
        # Bottom Up
        # dp = [0] * (target+1)
        # dp[0] = 1
        # for i in range(target+1):
        #     for num in sorted(nums):
        #         if i-num >= 0:
        #             dp[i] += dp[i-num]
        #         else:
        #             break
        # return dp[-1]