class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max1 = max2 = max3 = float('-inf')
        for integer in nums:
            if integer > max1:
                max1,max2,max3 = integer,max1,max2
            elif integer > max2:
                max2,max3 = integer,max2
            elif integer > max3:
                max3 = integer
        if max3 == float('-inf'):
            return max1
        else:
            return max3
