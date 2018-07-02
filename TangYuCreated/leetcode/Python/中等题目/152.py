class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCur = 1
        minCur = 1
        result = float('-inf')
        
        for num in nums:
            possible1 = num
            possible2 = num * maxCur
            possible3 = num * minCur
            
            maxCur = max(possible1,possible2,possible3)
            minCur = min(possible1,possible2,possible3)
            
            result = maxCur if maxCur > result else result
            
        return result
