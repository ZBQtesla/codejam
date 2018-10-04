class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        while k:
            print(k,matrix)
            result = matrix[0][0]
            matrix[0][0] = float('inf')
            k -= 1
            self.mend(matrix,0,0)
        return result
    def mend(self,matrix,row,column): #this function is used to mend the matrix after the extraction of the smallest element
        width = len(matrix[0])
        height = len(matrix)
        
        if row == height - 1:
            matrix[row][column:] = matrix[row][column + 1:] + [matrix[row][column]]
        elif column == width - 1:
            for row1 in range(height - 1,row,-1):
                matrix[row1 - 1][width - 1] = matrix[row1][width - 1]
            matrix[height - 1][width - 1] = float('inf')
        else:
            if matrix[row + 1][column] > matrix[row][column + 1]:
                matrix[row][column],matrix[row][column + 1] = matrix[row][column + 1],matrix[row][column]
                self.mend(matrix,row,column + 1)
            else:
                matrix[row][column],matrix[row + 1][column] = matrix[row + 1][column],matrix[row][column]
                self.mend(matrix,row + 1,column)

solution = Solution()
solution.kthSmallest([[1],
                      [2],
                      [3],
                      [4]
                      ],2)
