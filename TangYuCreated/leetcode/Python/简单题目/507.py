class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        factor = 1
        summation = 0
        while factor * factor <= num:
            if num % factor == 0:
                summation += factor + num // factor
                print(summation)
            factor += 1
                
        if (factor - 1)** 2 == num:
            summation -= factor - 1
        return num == summation - num
