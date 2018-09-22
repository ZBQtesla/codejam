class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        generator = maxFactor = int(n * '9')
        minFactor = int('1' + (n - 1) * '0')
        while True:
            possible = generator * 10 ** n
            tempGenerator = generator
            for i in range(n):
                possible += (tempGenerator % 10) * 10 ** (n - 1 - i)
                tempGenerator //= 10
            
            
            for factor in range(maxFactor,minFactor - 1,-1):
                if possible // factor > maxFactor:
                    break
                
                if possible % factor == 0:
                    return possible % 1337
            generator -= 1
            
