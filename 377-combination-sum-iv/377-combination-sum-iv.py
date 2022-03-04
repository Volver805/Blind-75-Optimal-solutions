from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize = None)
        def getCombinations(target):
            if target == 0:
                return 1
            res = 0
            for num in nums:
                newTarget = target-num
                if newTarget >= 0:
                    res += getCombinations(newTarget)    
            return res
        return getCombinations(target)