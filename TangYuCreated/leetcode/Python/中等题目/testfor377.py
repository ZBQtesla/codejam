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
                if num <= target:
                    reference[i] += reference[target - num]
                    print(reference)
        return reference[target]

solution = Solution()
solution.combinationSum4([1,2,3],4)
