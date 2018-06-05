class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            middle = (left + right) // 2
            result = middle * middle
            if result > x:
                right = middle - 1
            elif result < x:
                left = middle + 1
            else:
                return middle
        return left if left * left <= x else left - 1
