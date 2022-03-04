class Solution:
    def rob(self, nums: List[int]) -> int:
        neighbour = neighboursNeigbour = 0
        for i in reversed(range(len(nums))):
            curr = max(neighbour, neighboursNeigbour+nums[i])
            neighboursNeigbour = neighbour
            neighbour = curr
        return neighbour