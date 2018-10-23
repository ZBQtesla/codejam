class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for elementRow in range(3):
            for elementColumn in range(3):
                ref = set()
                for row in range(3 * elementRow,3 * elementRow + 3):
                    for column in range(3 * elementColumn,3 * elementColumn + 3):
                        if board[row][column].isdigit():
                            if board[row][column] in ref:
                                return False
                            ref.add(board[row][column])
                        
        for row in board:
            ref = set()
            for column in range(9):
                if row[column].isdigit():
                    if row[column] in ref:
                        return False
                    else:
                        ref.add(row[column])
                        
        for column in range(9):
            ref = set()
            for row in range(9):
                if board[row][column].isdigit():
                    if board[row][column] in ref:
                        return False
                    else:
                        ref.add(board[row][column])
        return True
