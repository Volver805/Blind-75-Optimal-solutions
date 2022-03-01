# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def iterateTree(node):
            nonlocal h
            if not node:
                return
            heapq.heappush(h, node.val)
            iterateTree(node.left)
            iterateTree(node.right)
        h = []
        iterateTree(root)
        return heapq.nsmallest(k, h)[-1]