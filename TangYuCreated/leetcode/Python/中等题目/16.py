class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length <= 3:
            return sum(nums)
        
        nums.sort()
        closest = float('inf')
        for left in range(length - 2):
            middle = left + 1
            right = length - 1
            while middle < right:
                possible = nums[left] + nums[right] + nums[middle]
                closest = possible if abs(possible - target) < abs(closest - target) else closest
                if possible < target:
                    middle += 1
                elif possible > target:
                    right -= 1
                else:
                    return possible
        return closest
                    
