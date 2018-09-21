class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for pos in range(len(A) - 1):
            if A[pos] > A[pos + 1]:
                return pos
        return len(A) - 1
