class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        height = -math.inf
        while left <= right:
            height = max(height, self.calculateWidth(nums,left, right))
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return height
        
    def calculateWidth(self,nums,start,end):
        return (end-start) * min(nums[start], nums[end])