class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        points = {}
        for i, move in enumerate(moves):
            row, col = move
            points[(row, col)] = i%2
            if self.checkForWinner(points, row, col): return ['A', 'B'][i%2]
        if len(points) == 9: return 'Draw'
        return 'Pending'
            
    def checkForWinner(self, points, row, col):
        if points.get((row, 0), -1) == points.get((row, 1), -2) == points.get((row, 2), -3) or points.get((0, col), -1) == points.get((1, col), -2) == points.get((2, col), -3):
                return True
        if points.get((0,0), -1) == points.get((1,1), -2) == points.get((2,2), -3) or points.get((0,2), -1) == points.get((1,1), -2) == points.get((2,0), -3):
            return True