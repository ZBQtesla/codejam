class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        length = len(nums)
        while index <= length - 1:
            while nums[index] != index + 1 and nums[nums[index] - 1] != nums[index]:
                num = nums[index]
                nums[index],nums[num - 1] = nums[num - 1],nums[index]
            index += 1
        for i in range(length):
            if nums[i] != i + 1:
                return [nums[i],i + 1]
