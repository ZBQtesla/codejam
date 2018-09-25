class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            element = nums[i]
            nums[abs(element)] = -nums[abs(element)]
            if nums[abs(element)] > 0:
                return abs(element)
