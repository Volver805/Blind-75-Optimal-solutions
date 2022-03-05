class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: 
            return []
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n-1))
        for i in range(n):
            pacific.add((0, i))
            atlantic.add((m-1, i))
        print(pacific)
        print(atlantic)
        
        def dfs(i, j, reachesOcean):
            reachesOcean.add((i, j))
            for (offsetBottom, offsetRight) in [(1,0), (-1, 0), (0, 1), (0,-1)]:
                newRow, newCol = i+offsetBottom, j+offsetRight
                if newRow == -1 or newCol == -1 or newRow == m or newCol == n:
                    continue
                if heights[newRow][newCol] < heights[i][j]:
                    continue
                if (newRow, newCol) in reachesOcean:
                    continue
                    
                dfs(newRow, newCol, reachesOcean)
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m - 1, i, atlantic)
        
        return list(pacific.intersection(atlantic))