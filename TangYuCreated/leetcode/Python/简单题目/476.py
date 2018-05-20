class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        length = 0
        h = num
        while num != 0:
            length += 1
            num >>= 1
        c = ~h
        return  c + 2 ** length
