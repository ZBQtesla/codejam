import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = n * [True] #representing 0,1,2,...,n - 1
        primes[0] = primes[1] = False
        for i in range(int(len(primes) ** 0.5) + 1):
            if primes[i]:
                primes[i ** 2::i] = [False] * len(primes[i ** 2::i])
        return sum(primes)
