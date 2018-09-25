class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        robTheLast = nums[-1] + self.robLinear(nums[1:-2])
        notTheLast = self.robLinear(nums[:-1])
        return max(robTheLast,notTheLast)
        
    def robLinear(self,nums):
        length = len(nums)
        if not length:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        reference = [nums[0],max(nums[0],nums[1])]
        for pos in range(2,length):
            reference.append(max(nums[pos] + reference[-2],reference[-1]))
        return reference[-1]
