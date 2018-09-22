class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        numRow = m
        numColumn = n
        
        for op in ops:
            numRow = min(op[0],numRow)
            numColumn = min(op[1],numColumn)
            
        return numRow * numColumn
