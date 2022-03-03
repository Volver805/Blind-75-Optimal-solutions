class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        res = []
            
        def backtracking(i, j, parent):
            char = board[i][j]
            node = parent[char]
            match = node.pop(WORD_KEY, False)
            if match:
                res.append(match)
            board[i][j] = '#' # this cell has been visited
            for bottom, right in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow, newCol = i+bottom, j+right
                if newRow < 0 or newCol < 0 or newRow == len(board) or newCol == len(board[0]):
                    continue
                if board[newRow][newCol] in node:
                    backtracking(newRow, newCol, node)
            board[i][j] = char
            if not node:
                parent.pop(char)
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word # Indicates the this is the end of a valid word
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return res