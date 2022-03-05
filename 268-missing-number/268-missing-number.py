class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
#         c = 0
#         for i in range(len(nums)+1):
#             c+=i
#         return c - sum(nums)

#       bit manipulation (optimal soultion)
        res = len(nums)
        for i, num in enumerate(nums):
            print(bin(res))
            res ^= i ^ num
        return res