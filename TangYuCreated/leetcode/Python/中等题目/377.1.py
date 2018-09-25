class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = []
        if target == 0:
            return [[]]
        else:
            for num in nums:
                if num <= target:
                    for combination in self.combinationSum4(nums,target - num):
                        result.append([num] + combination)
            return result
