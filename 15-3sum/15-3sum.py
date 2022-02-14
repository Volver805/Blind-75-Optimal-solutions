class Solution:
    def threeSum(self, nums: List[int]):
        res = []
        for i in range(len(nums)):
            target = nums[i]
            s = set()
            for j in range(i+1, len(nums)):
                comp = -target - nums[j]
                if comp in s:
                    x = sorted([target, nums[j], comp])
                    if x not in res:
                        res.append(x)
                s.add(nums[j])
        return res