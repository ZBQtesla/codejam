class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        initial = nums[0]
        last = nums[0]
        for num in nums:
            if num <= last + 1:
                last = num
            else:
                if initial == last:
                    result.append(str(initial))
                else:
                    result.append(str(initial) + '->' + str(last))
                initial = last = num
        else:
            if initial == last:
                result.append(str(initial))
            else:
                result.append(str(initial) + '->' + str(last))
        return result
