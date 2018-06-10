class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = len(nums) * [1]
        for i in range(len(nums) - 2,-1,-1):
            right[i] = right[i + 1] * nums[i + 1]
        left = 1
        for i in range(len(nums)):
            right[i] *= left
            left *= nums[i]
        return right
