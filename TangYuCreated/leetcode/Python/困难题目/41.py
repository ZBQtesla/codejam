class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        length = len(nums)
        focus = 0
        while focus <= length - 1:
            element = nums[focus]
            if element == focus + 1:
                focus += 1
                continue
                
            if element > 0 and element < length + 1:
                if nums[element - 1] != element:
                    nums[element - 1],nums[focus] = element,nums[element - 1]
                else:
                    focus += 1
            else:
                focus += 1
                
        for position in range(length):
            if nums[position] != position + 1:
                return position + 1
        return length + 1
