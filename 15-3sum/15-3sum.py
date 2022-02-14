class Solution:
    def threeSum(self, nums: List[int]):
        res, dups = set(), set()
        for i in range(len(nums)):
            target = nums[i]
            if nums[i] not in dups:
                dups.add(nums[i])
                s = set()
                for j in range(i+1, len(nums)):
                    comp = -target - nums[j]
                    if comp in s:
                        res.add(tuple(sorted([target, nums[j], comp])))
                    s.add(nums[j])
        return res