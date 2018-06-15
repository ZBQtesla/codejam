class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        uplist = [1]
        downlist = [1]
        length = 1
        for num in nums[1:]:
            maxup = maxdown = 1
            for i in range(length):
                if num > nums[i]:
                    maxdown = max(1 + uplist[i],maxdown)
                elif num < nums[i]:
                    maxup = max(1 + downlist[i],maxup)
            uplist.append(maxup)
            downlist.append(maxdown)
            length += 1
        return max(max(uplist),max(downlist))
