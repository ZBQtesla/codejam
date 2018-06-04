class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            isneg = True
            num = -num
        else:
            isneg = False
        bitList = []
        while num != 0:
            bitList.insert(0,str(num % 7))
            num //= 7
        result = ''
        if isneg:
            result += '-'
        for bit in bitList:
            result += bit
        return result
