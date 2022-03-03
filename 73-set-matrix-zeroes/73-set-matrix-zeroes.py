class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
                    
        for i in rows:
            matrix[i] = [0]* len(matrix[i])
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return matrix
            