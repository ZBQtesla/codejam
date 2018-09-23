class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid[0])
        height = len(grid)
        result = [
            [0] * width for i in range(height)
        ]
        result[height - 1][width - 1] = grid[height - 1][width - 1]
        
        for column in range(width - 2,-1,-1):
            result[height - 1][column] = grid[height - 1][column] + result[height - 1][column + 1]
        for row in range(height - 2,-1,-1):
            result[row][width - 1] = grid[row][width - 1] + result[row + 1][width - 1]
            
        for row in range(height - 2,-1,-1):
            for column in range(width - 2,-1,-1):
                result[row][column] = grid[row][column] + min(result[row + 1][column],result[row][column + 1])
        return result[0][0]
