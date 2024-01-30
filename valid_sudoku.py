board = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]
]

class Solution:
    def row_checker(self, board):
        for i in range(9):
            d = {}
            for j in range(9):
                number = board[i][j]
                if number.isdigit():
                    d[number]= d.get(number, 0) + 1
                    if d[number] > 1:
                        return False
        return True
    
    def column_checker(self, board):
        for i in range(9):
            d = {}
            for j in range(9):
                number = board[j][i]
                if number.isdigit():
                    d[number] = d.get(number, 0) + 1
                    if d[number] > 1:
                        return False
        return True
    
    def grid_checker(self, board):
        for i in range(3):
            for j in range(3):
                d = {}
                for k in range(i * 3, (i + 1) * 3):
                    for l in range(j * 3, (j + 1) * 3):
                        number = board[k][l]
                        if number.isdigit():
                            d[number] = d.get(number, 0) + 1
                            if d[number] > 1:
                                return False
        return True
    
    

    
    def isValidSudoku(self, board) -> bool: 
        if self.grid_checker(board) and self.column_checker(board) and self.row_checker(board):
            return True 
        return False
                
