class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expect = n * (n + 1) // 2
        return expect - sum(nums)
