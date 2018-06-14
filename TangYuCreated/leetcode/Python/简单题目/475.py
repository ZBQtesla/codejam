class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if not houses:
            return 0
        
        houses.sort()
        heaters.sort()
        result = 0
        position = self.searchInsert(heaters,houses[0])
        lengthHeater = len(heaters)
        
        for house in houses:
            while position < lengthHeater and house > heaters[position]:
                position += 1
            if position == lengthHeater:
                result = max(house - heaters[-1],result)
            elif position == 0:
                result = max(heaters[0] - house,result)
            else:
                result = max(min(house - heaters[position - 1],heaters[position] - house),result)
        return result
                
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        length = len(nums)
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return length
        
        #assume that this nums is long,and the position of the insertion is within the list
        left = 0
        right = length - 1
        while True:
            middle = (left + right) // 2
            if nums[middle] < target <= nums[middle + 1]:
                return middle + 1
            elif target <= nums[middle]:
                right = middle
            else:
                left = middle + 1
