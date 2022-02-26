# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        s = []
        def bfs(root, c=0):
            nonlocal s
            if not root:
                return
            if len(s) > c:
                s[c].append(root.val)
            else:
                s.append([root.val])
            bfs(root.left, c+1)
            bfs(root.right, c+1)
            return s
        bfs(root)
        return s
        
    