class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length = len(nums)
       
        for i in range(length):
            nums[i] = [nums[i],i]
        listnums = sorted(nums,key = lambda x:x[0],reverse = True)
        
        for i in range(length):
            if i >= 3:
                listnums[i][0] = str(i + 1)
            elif i == 0:
                listnums[i][0] = "Gold Medal" 
            elif i == 1:
                listnums[i][0] = "Silver Medal"
            elif i == 2:
                listnums[i][0] = "Bronze Medal"
        
        liststring = sorted(listnums,key = lambda x:x[1])
        result = []
        
        for i in range(length):
            result.append(liststring[i][0])
            
        return result
