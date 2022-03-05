class Node:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
        
        
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dp = set()
        nodes = [None]*numCourses
        for i in range(numCourses):
            nodes[i] = Node(i, [])
        for course, prerequisite in prerequisites:
            nodes[prerequisite].neighbors.append(nodes[course])
        def explore(node):
            if node.val in dp:
                return True
            if node.val == '#':
                return False
            val = node.val
            node.val = '#'
            for n in node.neighbors:
                if not explore(n):
                    return False
            node.val = val
            dp.add(node.val)
            return True
            
        for node in nodes:
            if not explore(node):
                return False
        return True
