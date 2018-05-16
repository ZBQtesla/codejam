class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        result = nums[0]
        
        for i in range(1,len(nums)):
            result ^= nums[i]
        return result
