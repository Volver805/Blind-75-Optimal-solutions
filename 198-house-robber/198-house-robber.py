class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        @functools.lru_cache(maxsize = None)
        def test(i, money=0):
            if i >= len(nums):
                return money
            money += nums[i]
            return max(test(i+2, money), test(i+3, money))
        return max(test(0), test(1))