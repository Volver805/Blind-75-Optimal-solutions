class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = maxSum = minSum = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], maxSum * nums[i], minSum * nums[i])
            minSum = min(nums[i], maxSum * nums[i], minSum * nums[i])
            maxSum = temp # we used a temporary variable because we need the old value of maxSum to calculate minSum
            maxProduct = max(maxSum, maxProduct)
        return maxProduct