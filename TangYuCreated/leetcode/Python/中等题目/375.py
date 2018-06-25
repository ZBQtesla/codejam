class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        reference = [[float('inf')] * (n + 1) for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(i + 1):
                reference[i][j] = 0
        
        for length in range(2,n + 1):
            for begin in range(1,n + 2 - length):
                end = length + begin - 1
                reference[begin][end] = min([choice + max(reference[begin][choice - 1],reference[choice + 1][end]) for choice in range(begin,end)])
        return reference[1][n]
