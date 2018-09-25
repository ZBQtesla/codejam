class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        reference = [1] + [0] * (target)
        for i in range(1,target + 1):
            for num in nums:
                if num <= i:
                    reference[i] += reference[i - num]
        return reference[target]
