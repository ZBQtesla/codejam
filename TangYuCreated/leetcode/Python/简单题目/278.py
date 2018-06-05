# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            middle = (left + right) // 2
            
            badMiddle = isBadVersion(middle)
            badMiddleRight = isBadVersion(middle + 1)
            
            if badMiddleRight and not badMiddle:
                return middle + 1
            elif badMiddleRight:
                right = middle
            else:
                left = middle + 1
        return left
