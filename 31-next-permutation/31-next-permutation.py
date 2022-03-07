class Solution:
    def nextPermutation(self, nums) -> None :
        br = False
        i = len(nums)-1
        while i != 0:
            if nums[i] > nums[i-1]:
                i-=1
                br = True
                break
            i-=1
        if not br:
            nums.sort()
            return
        j = len(nums)-1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])