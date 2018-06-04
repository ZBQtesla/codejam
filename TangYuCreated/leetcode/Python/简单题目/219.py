class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
            else:
                dic[nums[i]] = i
            i += 1
        return False
