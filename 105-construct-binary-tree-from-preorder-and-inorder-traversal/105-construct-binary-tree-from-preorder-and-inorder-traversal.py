# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            nonlocal preorderPointer
            
            if left > right:
                return
            val = preorder[preorderPointer]
            node = TreeNode(val)
            preorderPointer += 1
            
            node.left = construct(left, lookUp[val]-1)
            node.right = construct(lookUp[val]+1, right)
            return node
            
            return node
        lookUp = {}
        for i in range(len(inorder)):
            lookUp[inorder[i]] = i
        preorderPointer=0
        return construct(0, len(inorder)-1)
    