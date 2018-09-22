class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        width = len(A[0])
        height = len(A)
        result = 0
        for row in range(height):
            if not A[row][0]:
                for column in range(width):
                    A[row][column] = 1 if not A[row][column] else 0
        for column in range(width):
            numOfOne = [row[column] for row in A].count(1)
            result += max(numOfOne,height - numOfOne) * 2 ** (width - 1 - column)
        return result
