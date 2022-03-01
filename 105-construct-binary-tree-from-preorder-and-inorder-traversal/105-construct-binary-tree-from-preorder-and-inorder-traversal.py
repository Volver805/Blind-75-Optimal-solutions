# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookUp = {}
        for i in range(len(inorder)):
            lookUp[inorder[i]] = i
        return self.attachSubtree(preorder, inorder, lookUp, 0, len(inorder))
    
    def attachSubtree(self, preorder, inorder, lookUp, left, right):
        if not preorder:
            return
        pos = lookUp[preorder[0]]
        if pos < left or pos > right:
            return self.attachSubtree(preorder[1:], inorder, lookUp, left, right)
        node = TreeNode(preorder.pop(0))
        node.left = self.attachSubtree(preorder, inorder, lookUp, left, pos)
        node.right = self.attachSubtree(preorder, inorder, lookUp, pos, right)
        return node