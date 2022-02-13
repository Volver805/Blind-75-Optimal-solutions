class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        size = len(nums)
        lC = rC = 1
        for i in range(size):
            l[i] = lC
            lC *= nums[i]
            r[size-1-i] = rC
            rC *= nums[size-1-i]
        for i in range(len(nums)):
            nums[i] = l[i] * r[i]
        return nums