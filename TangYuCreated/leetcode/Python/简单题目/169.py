class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = nums[0]
        number = 0
        
        for num in nums:
            if element == num:
                number += 1
            elif number:
                number -= 1
            else:
                element = num
                number = 1
        return element
