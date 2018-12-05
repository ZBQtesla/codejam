class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #we go from back to the head of the list
        length = len(nums)
        if length < 3:
            return False
        second = nums[-1]
        
        stack = list()
        stack.append(float('inf'))
        #head of the stack being stack[-1]
        found = False
        for num in nums[len(nums) - 2::-1]:
            if num < second:
                if found:
                    return True
                else:
                    stack.append(second)
                    second = num
            elif num > second:
                found = True
                while num > stack[-1]:
                    second = stack.pop()
                stack.append(num)
        return False
            
