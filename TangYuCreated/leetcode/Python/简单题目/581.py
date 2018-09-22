class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        findFirst = False
        length = len(nums)
        for pos in range(len(nums) - 1):
            if nums[pos] > nums[pos + 1]:
                if not findFirst:
                    findFirst = True
                    firstPos = pos
                lastPos = pos + 1
        
        if not findFirst:
            return 0
        
        subMax,subMin= max(nums[firstPos:lastPos + 1]),min(nums[firstPos:lastPos + 1])
        
        while True:
            state = False
            if firstPos and nums[firstPos - 1] > subMin:
                firstPos -= 1
                subMax = max(subMax,nums[firstPos])
                state = True
            
            if lastPos != length - 1 and nums[lastPos + 1] < subMax:
                lastPos += 1
                subMin = min(subMin,nums[lastPos])
                state = True
                
            if not state:
                return lastPos - firstPos + 1
