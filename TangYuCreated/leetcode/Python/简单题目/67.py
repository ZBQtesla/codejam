class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1 = int(a,base = 2) + int(b,base = 2)
        result = bin(sum1)[2:]
        return result
