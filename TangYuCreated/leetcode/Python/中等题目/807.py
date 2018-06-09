class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid[0])
        upper = col * [0]
        for row in grid:
            for column in range(col):
                upper[column] = row[column] if row[column] > upper[column] else upper[column]
        left = [max(row) for row in grid]
        i = j = 0
        count = 0
        while i <= col - 1:
            j = 0
            while j <= col - 1:
                count += min(left[i],upper[j]) - grid[i][j]
                grid[i][j] = min(left[i],upper[j])
                j+= 1
            i += 1
        return count
        
