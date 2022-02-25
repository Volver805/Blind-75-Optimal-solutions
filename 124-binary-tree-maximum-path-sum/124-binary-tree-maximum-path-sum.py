# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = -math.inf
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.calculatePathSum(root)
        return self.result
    
    def calculatePathSum(self, node):
        if not node:
            return -math.inf
        left = self.calculatePathSum(node.left)
        right = self.calculatePathSum(node.right)
        biggerNodeResult = max(left, right)
        if biggerNodeResult < 0:
            self.result = max(node.val, self.result)
            return node.val
        else:
            self.result = max(self.result, node.val + biggerNodeResult, node.val + left + right)
            return node.val + biggerNodeResult