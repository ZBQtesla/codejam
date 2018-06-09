class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        else:
            sub = []
            for i in range(len(nums)):
                sub.extend([ [nums[i]] + set1 for set1 in self.subsets(nums[i + 1:])  ])
            sub.append([])
            return sub
