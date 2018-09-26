class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        appearance = 0
        pos = 0
        present = None
        
        while pos < length:
            if nums[pos] == present:
                if appearance == 2:
                    for i in range(pos,length - 1):
                        nums[i] = nums[i + 1]
                    length -= 1
                else:
                    appearance += 1
                    pos += 1
            else:
                appearance = 1
                present = nums[pos]
                pos += 1
        return length
