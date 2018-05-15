class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        height = len(matrix)
        width = len(matrix[0])
        
        for row in range(height - 1,-1,-1):
            rownow = row
            i = 0   #current column
            while rownow + 1 < height and i + 1 < width:
                if matrix[rownow + 1][i + 1] != matrix[rownow][i]:
                    return False     
                rownow += 1
                i += 1
                
        for column in range(0,width):
            columnnow = column
            j = 0   #current row
            while columnnow + 1 < width and j + 1 < height:
                if matrix[j + 1][columnnow + 1] != matrix[j][columnnow]:
                    return False
                columnnow += 1
                j += 1
                
        return True
