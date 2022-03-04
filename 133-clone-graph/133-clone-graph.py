"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def cloneNode(node, created):
            newNode = Node(node.val)
            created[newNode.val] = newNode
            for neighbor in node.neighbors:
                if neighbor.val in created:
                    newNode.neighbors.append(created[neighbor.val])
                else:
                    newNode.neighbors.append(cloneNode(neighbor, created))
            return newNode
        if not node:
            return
        return cloneNode(node, {})    