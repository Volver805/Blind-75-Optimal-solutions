class Solution:
    def twoSum(self, nums, target: int):
        hashMap = {}
        for i, num in enumerate(nums):
            comp = target-num
            if num in hashMap:
                return [hashMap[num], i]
            hashMap[comp] = i