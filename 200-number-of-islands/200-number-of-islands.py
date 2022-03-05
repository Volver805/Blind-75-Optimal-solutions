class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        m, n = len(grid), len(grid[0])
                
        def dfs(i, j):
            if grid[i][j] != '1':
                return
            grid[i][j] = '#' # this cell of land was visited
            for offsetBottom, offsetRight in [(1,0),(0,1),(-1,0),(0,-1)]:
                newRow, newCol = i+offsetBottom, j+offsetRight
                if newRow == -1 or newCol == -1 or newRow == m or newCol == n:
                    continue
                dfs(newRow, newCol)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    c += 1
                    dfs(i, j)
        
        return c