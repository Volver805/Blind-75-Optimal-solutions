class Solution:
    def findMin(self, nums: List[int]) -> int:
        f = nums[0]
        left = 0  
        right = len(nums) -1
        
#         if nums[right] > nums[0]:
#             return nums[0]
        
        while left < right:
            x = (right + left) // 2
            if nums[x] > nums[x+1]:
                return nums[x+1]
            elif nums[x] < nums[x-1]:
                return nums[x]
            elif nums[x] > f:
                left = x+1
            else:
                right = x-1
        return nums[0]
                