class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n == 3:
                count += 2
                return count
            if not n & 1:
                n = n >> 1
                count += 1
            else:
                if n & 3 == 3:
                    n = n + 1
                    count += 1
                else:
                    n = n - 1
                    count += 1
        return count
