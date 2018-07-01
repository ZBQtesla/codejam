class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = [float('-inf')] * k
        for num in nums:
            result.insert(self.searchInsert(result,num),num)
            result.pop()
        return result[-1]
        
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        length = len(nums)
        if target >= nums[0]:
            return 0
        elif target < nums[-1]:
            return length
        
        #assume that this nums is long,and the position of the insertion is within the list
        left = 0
        right = length - 1
        while True:
            middle = (left + right) // 2
            if nums[middle] > target >= nums[middle + 1]:
                return middle + 1
            elif target >= nums[middle]:
                right = middle
            else:
                left = middle + 1
