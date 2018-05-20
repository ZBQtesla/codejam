class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumn = 0
        while n != 0:
            sumn += n // 5
            n //= 5
        return sumn
