class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        return len(set(nums)) != len(nums)
