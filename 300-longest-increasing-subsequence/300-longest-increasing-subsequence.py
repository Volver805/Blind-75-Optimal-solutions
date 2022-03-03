class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DYNAMIC PROGRAMMING SOLUTION
        # dp = [1]*len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        subsequence = [nums[0]]
        for i in range(1, len(nums)):
                if nums[i] > subsequence[-1]:
                    subsequence.append(nums[i])
                else:
                    j = 0
                    while nums[i] > subsequence[j]:
                        j += 1
                    subsequence[j] = nums[i]
        return len(subsequence)