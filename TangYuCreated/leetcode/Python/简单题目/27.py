class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        for i in range(nums.count(val)):
            nums.remove(val)
            length -= 1
        return length
