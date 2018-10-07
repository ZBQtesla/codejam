class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row = click[0]
        column = click[1]
        if board[row][column] == 'M':
            board[row][column] = 'X'
            return board
        width = len(board[0])
        height = len(board)
        
        if board[row][column] == 'E':
            count = 0
            for row0,column0 in [(row1,column1) for row1 in {row,min(row + 1,height - 1),max(row - 1,0)} for column1 in {column,min(width - 1,column + 1),max(0,column - 1)}]:
                if board[row0][column0] == 'M':
                    count += 1
            
            if not count:
            
                board[row][column] = 'B'
                for row0,column0 in [(row1,column1) for row1 in {row,min(row + 1,height - 1),max(row - 1,0)} for column1 in {column,min(width - 1,column + 1),max(0,column - 1)}]:
                    self.updateBoard(board,[row0,column0])
            else:
                board[row][column] = str(count)
        return board
