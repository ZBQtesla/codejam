class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sumraw = 0
        
        height = len(grid)
        width = len(grid[0])
        if height == 1:
            return 2 * grid[0].count(1) + 2
        for i in range (height):
            sumraw += grid[i].count(1)
        if width == 1:
            return grid.count([1]) * 2 + 2
        sumraw *= 4
        
        for row in range(1,height):
            for column in range(width):
                if grid[row][column] == 1 and grid[row - 1][column] == 1:
                        sumraw -= 2
        for column in range(1,width):
            for row in range(height):
                if grid[row][column] == 1 and grid[row][column - 1]:
                    sumraw -= 2
        return sumraw
