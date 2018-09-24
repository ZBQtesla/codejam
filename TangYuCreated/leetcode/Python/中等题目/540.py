class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if (right - left) // 2 % 2 == 0:
                if nums[middle] == nums[middle + 1]:
                    left = middle + 2
                elif nums[middle] == nums[middle - 1]:
                    right = middle - 2
                else:
                    return nums[middle]
            else:
                if nums[middle] == nums[middle + 1]:
                    right = middle - 1
                elif nums[middle] == nums[middle - 1]:
                    left = middle + 1
                else:
                    return nums[middle]
        return nums[left]
