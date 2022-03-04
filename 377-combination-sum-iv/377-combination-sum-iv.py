class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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