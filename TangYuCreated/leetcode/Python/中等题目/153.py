class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        left = 0
        right = length - 1
        if nums[left] < nums[right]:
            return nums[left]
        else:
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] > nums[middle + 1]:
                    return nums[middle + 1]
                else:
                    if nums[middle] > nums[right]:
                        left = middle + 1
                    else:
                        right = middle
        
