class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        width = len(board[0])
        height = len(board)
        if not width:
            return 0
        result = 0
        for column in range(1,width):
            if board[0][column] == 'X' and board[0][column - 1] != 'X':
                result += 1
        for row in range(1,height):
            if board[row][0] == 'X' and board[row - 1][0] != 'X':
                    result += 1
        for row in range(1,height):
            for column in range(1,width):
                if board[row][column] == 'X' and board[row - 1][column] != 'X' and board[row][column - 1] != 'X':
                    result += 1
        result += board[0][0] == 'X'
        return result
