class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        # We can consider this solution O(1) as this problem states 
        # that the output array does not count as an extra space.
        res = [1]*size
        for i in range(1, size):
            res[i] = nums[i-1] * res[i-1]
        R = nums[-1]
        for i in range(size-2, -1, -1):
            nums[i], R = R*res[i], nums[i] * R
        nums[-1] = 1 * res[-1]
        return nums