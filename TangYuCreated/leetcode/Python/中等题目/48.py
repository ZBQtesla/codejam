class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width = height = len(matrix)
        for row in range((height + 1) // 2):
            for column in range(row,width - 1 - row):
                matrix[row][column],matrix[column][width - 1 - row],matrix[height - 1 - row][width - 1 - row - (column - row)],\
                matrix[height - 1 - row - (column - row)][row] = \
                matrix[height - 1 - row - (column - row)][row],matrix[row][column],matrix[column][width - 1 - row],matrix[height - 1 - row][width - 1 - row - (column - row)]
        
