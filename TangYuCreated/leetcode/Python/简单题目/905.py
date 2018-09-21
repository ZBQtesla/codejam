class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        pos = 0
        for focus in range(len(A)):
            if A[focus] % 2 == 0:
                A[pos],A[focus] = A[focus],A[pos]
                pos += 1
        return A
