class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        else:
            result = [
                [0] * n for i in range(m)
            ]
            result[m - 1] = [1] * n
            for row in range(m - 2,-1,-1):
                result[row][n - 1] = 1
                for column in range(n - 2,-1,-1):
                    result[row][column] = result[row + 1][column] + result[row][column + 1]
            return result[0][0]
