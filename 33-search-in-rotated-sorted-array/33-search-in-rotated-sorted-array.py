class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = nums[0]
        left = 0
        right = len(nums)-1
        if target == f:
            return 0
        while left <= right:
            x = left + (right - left) // 2
            if nums[x] == target:
                return x
            if target > f:
                if nums[x] < f or nums[x] > target:
                    right = x-1
                else:
                    left = x+1
            if target < f:
                if nums[x] >= f or nums[x] < target:
                    left = x+1
                else:
                    right = x-1
        return -1
        
                
                