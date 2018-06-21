class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        realA,imagA = int(a.split('+')[0]),int(a.split('+')[1][:-1])
        realB,imagB = int(b.split('+')[0]),int(b.split('+')[1][:-1])
        realResult = realA * realB - imagA * imagB
        imagResult = realA * imagB + realB * imagA
        return str(realResult) + '+' + str(imagResult) + 'i'
