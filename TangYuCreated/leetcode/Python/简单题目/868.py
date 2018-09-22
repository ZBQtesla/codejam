class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 0
        maxLength = 0
        N = bin(N)[2:]
        previous = present = 0
        
        for focus in range(1,len(N)):
            if N[focus] == '1':
                previous,present = present,focus
                maxLength = max(maxLength,present - previous)
        
        return maxLength
