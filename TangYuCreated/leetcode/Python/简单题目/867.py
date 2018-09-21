class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [
            [None] * len(A) for i in range(len(A[0]))
        ]
        for row in range(len(A)):
            for column in range(len(A[0])):
                B[column][row] = A[row][column]
        return B
