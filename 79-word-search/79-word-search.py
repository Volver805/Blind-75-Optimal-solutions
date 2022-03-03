class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.search(word[1:], board, i, j):
                        return True
        return False
        
    def search(self, word, board, i, j):
        if len(word) == 0:
            return True
        ch = board[i][j]
        board[i][j] = '#'
        for bottom, right in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            newRow, newCol = i+bottom, j+right
            if newRow < 0 or newCol < 0 or newRow == len(board) or newCol == len(board[0]):
                continue
            if board[newRow][newCol] == word[0]:
                if self.search(word[1:], board, newRow, newCol):
                    return True
        board[i][j] = ch
#         if i < 0 or j < 0 or i == len(board) or j == len(board[i]): return
#         if (i, j) in visited: return
#         if word[0] != board[i][j]: return
#         if len(word) == 1:
#             return True
#         visited.add((i, j))
#         top = self.search(word[1:], board, i-1, j, visited.copy())
#         bottom = self.search(word[1:], board, i, j-1, visited.copy())
#         left = self.search(word[1:], board, i+1, j, visited.copy())
#         right = self.search(word[1:], board, i, j+1, visited.copy())
        
#         return top or bottom or left or right