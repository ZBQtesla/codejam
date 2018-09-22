class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [
            [0] * n for i in range(n)
        ]
        direction = 'right'
        nowRow = 0
        nowCol = -1
        element = 1
        
        while element <= n ** 2:
            if direction == 'right':
                matrix[nowRow][nowCol + 1] = element
                nowCol += 1
                element += 1
                if nowCol == n - 1 or matrix[nowRow][nowCol + 1]:
                    direction = 'down'
            elif direction == 'down':
                matrix[nowRow + 1][nowCol] = element
                nowRow += 1
                element += 1
                if nowRow == n - 1 or matrix[nowRow + 1][nowCol]:
                    direction = 'left'
            elif direction == 'left':
                matrix[nowRow][nowCol - 1] = element
                nowCol -= 1
                element += 1
                if nowCol == 0 or matrix[nowRow][nowCol - 1]:
                    direction = 'up'
            elif direction == 'up':
                matrix[nowRow - 1][nowCol] = element
                nowRow -= 1
                element += 1
                if nowRow == 0 or matrix[nowRow - 1][nowCol]:
                    direction = 'right'
                
        return matrix
