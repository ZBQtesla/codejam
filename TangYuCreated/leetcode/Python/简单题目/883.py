class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return (len(grid) * len(grid[0]) - sum([row.count(0) for row in grid])) + sum([max([row[i] for row in grid]) for i in range(len(grid[0]))]) + sum([max(row) for row in grid])
