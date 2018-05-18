class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        elif num == 1:
            return True
        if num & (num - 1):
            return False
        if num & 0b10101010101010101010101010101010:
            return False
        return True
