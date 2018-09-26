class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = []
        for pos in range(length):
            element = abs(nums[pos])
            nums[element - 1] = -nums[element - 1]
            if nums[element - 1] > 0:
                result.append(element)
        return result
