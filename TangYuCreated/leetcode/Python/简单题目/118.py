class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #result[row][column] = result[row - 1][column] + ..[column - 1]
        #we have to operate on the result from numRows >= 3
        if numRows == 0:
            return []
        if numRows == 1:
            return [
                [1]
            ]
        elif numRows == 2:
            return [
                [1],
                [1,1]
            ]
        result = []
    
        #initialization
        result.append([1])
        result.append([1,1])
        
        for row in range(2,numRows):    #we will manipulate every row
            result.append((row + 1) * [1])
            for column in range(1,row):
                result[row][column] = result[row - 1][column] + result[row - 1][column - 1]
                
        return result
