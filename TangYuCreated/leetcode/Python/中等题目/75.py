class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first = second = third = 0
        present = 0
        length = len(nums)
        while length - present:
            if nums[present] == 0:
                first += 1
                nums[first - 1] = 0
                
                if second:
                    nums[second] = 1
                    second += 1
                if third:
                    nums[third] = 2
                    third += 1
            elif nums[present] == 1:
                if not second:
                    second = first
                
                nums[second] = 1
                second += 1
                if third:
                    nums[third] = 2
                    third += 1
            else:
                if not third:
                    third = max(second,first)
                third += 1
            present += 1
