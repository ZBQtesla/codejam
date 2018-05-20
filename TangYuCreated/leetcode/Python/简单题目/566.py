class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        listonedim = []
        for row in nums:
            listonedim.extend(row)
        row = 0
        result = []
        index = 0
        while row < r:
            column = 0
            result.append([])
            while column < c:
                result[row].append(listonedim[index])
                index += 1
                column += 1
            row += 1
        return result
                
