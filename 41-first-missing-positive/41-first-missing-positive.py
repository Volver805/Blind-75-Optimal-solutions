class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = 1
        k = []
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] == s:
                    s += 1
                    while len(k) > 0 and k[0] <= s:
                        l = heapq.heappop(k)
                        if l == s:
                            s += 1
                elif nums[i] < s:
                    continue
                else:
                    heapq.heappush(k, nums[i])
        return s