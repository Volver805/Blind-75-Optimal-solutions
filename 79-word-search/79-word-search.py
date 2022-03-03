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