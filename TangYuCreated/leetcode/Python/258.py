class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = num
        while result >= 10: #we should operate on the result
            sumi = 0    #the sum of the numbers
            result1 = result
            while result1 > 0:
                sumi += result1 % 10
                result1 //= 10
            result = sumi
            
        return result
