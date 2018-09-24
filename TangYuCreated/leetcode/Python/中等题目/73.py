class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        for row in matrix:
            for column in range(width):
                if not row[column]:
                    row[column] = None
        for row in range(height):
            for column in range(width):
                if matrix[row][column] == None:
                    matrix[row][column] = 0
                    for row1 in range(height):
                        if matrix[row1][column] != None:
                            matrix[row1][column] = 0
                    for column1 in range(width):
                        if matrix[row][column1] != None:
                            matrix[row][column1] = 0
