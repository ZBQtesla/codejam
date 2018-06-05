class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        middle = (left + right) // 2
        while left < right:
            tempResult = middle * middle
            if tempResult == num:
                return True
            elif tempResult < num:
                left = middle + 1
            else:
                right = middle - 1
            middle = (left + right) // 2
        return left * left == num
        
