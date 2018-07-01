class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length == 1:
            return triangle[0][0]
        shortestPath = []
        for val in triangle[-1]:
            shortestPath.append(val)
        for row in range(length-2,-1,-1):
            for col in range(row + 1):
                shortestPath[col] = triangle[row][col] + min(shortestPath[col], shortestPath[col + 1])
        return shortestPath[0]
