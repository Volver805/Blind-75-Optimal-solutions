# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.matchTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
    def matchTree(self, root, sub):
        if not root and not sub:
            return True
        if not root or not sub:
            return False
        if root.val == sub.val:
            return self.matchTree(root.left, sub.left) and self.matchTree(root.right, sub.right)
        return False