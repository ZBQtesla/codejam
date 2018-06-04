class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = 1
        coins = 1
        while coins < n:
            result += 1
            coins += result
        if coins == n:
            return result
        else:
            return result - 1
