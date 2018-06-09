class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        primeDivisor = []
        while n != 1:
            for i in range(2,n + 1):
                if n % i == 0:
                    primeDivisor.append(i)
                    n = n // i
                    break
        return sum(primeDivisor)
