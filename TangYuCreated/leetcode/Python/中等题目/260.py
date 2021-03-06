class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        reference = 0
        position = 0
        for num in nums:
            reference ^= num
        for pos in range(32):
            if reference & 1:
                position = pos
                break
                
            reference >>= 1
        result1 = result2 = 0
        for num in nums:
            if num & (2 ** position):
                result1 ^= num
            else:
                result2 ^= num
        return [result1,result2]
