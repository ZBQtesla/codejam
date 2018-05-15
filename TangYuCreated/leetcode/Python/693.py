class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = []
        if n == 0 or n == 1:
            return True
        while n != 0:
            result.append(n % 2)
            n //= 2
            
        for i in range(len(result) - 1):
            if result[i] == result[i + 1]:
                return False
        return True
