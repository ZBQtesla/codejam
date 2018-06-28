class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = ''
        while n:
            string = chr(ord('A') + (n - 1) % 26) + string
            n = (n - 1) // 26
        return string
