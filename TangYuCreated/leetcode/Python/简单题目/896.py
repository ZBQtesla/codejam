class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        if length == 1:
            return True
        
        if A[0] == A[-1]:
            compare = A[0]
            for num in A:
                if num != compare:
                    return False
            else:
                return True
        elif A[0] > A[-1]:
            for i in range(length - 1):
                if A[i] < A[i + 1]:
                    return False
            else:
                return True
        else:
            for i in range(length - 1):
                if A[i] > A[i + 1]:
                    return False
            else:
                return True
