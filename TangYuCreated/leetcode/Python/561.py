class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sumn = 0
        for i in range(0,len(nums),2):
            sumn += nums[i]
            
        return sumn
