class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if length <= 2:
            return list(set(nums))
        
        n1,n2 = 0,0
        c1,c2 = 0,0
        
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 * c2:
                c1 -= 1
                c2 -= 1
            else:
                if c1 == 0:
                    n1 = num
                    c1 = 1
                else:
                    n2 = num
                    c2 = 1
        c1 = c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
        result = []
        if c1 > length / 3:
            result.append(n1)
        if c2 > length / 3:
            result.append(n2)
        return result
