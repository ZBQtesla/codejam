class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        listtrue = []
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                listtrue.append((1,i + 1))
                
        if len(listtrue) >= 2:
            return False
        elif len(listtrue) == 1 and listtrue[0][1] != len(nums) - 1:    #len >= 3 here
            target = listtrue[0][1]
            if nums[target + 1] < nums[target - 1]: #we cannont operate on the middle element
                if target != 1 and nums[target - 2] > nums[target]: #we cannot operate on the left element
                    return False
        return True
