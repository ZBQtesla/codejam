class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #The algorithmic idea behind this problem is to use two-pointer algorithm
        #the leftmost number will be nums(k),and i in the middle.
        #to avoid repetition,when nums(k) == nums(k - 1),we simply skip k
        #result:list of tuples
        
        #sort first
        nums.sort()
        lennums = len(nums)
        result = []
        for i in range(lennums - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                j = i + 1
                k = lennums - 1
                while j < k:
                    acc = nums[i] + nums[j] + nums[k]
                    if acc == 0:
                        result.append((nums[i] , nums[j] , nums[k]))
                        j += 1
                        k -= 1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
                        while nums[k] == nums[k + 1] and j < k:
                            k -= 1
                    elif acc < 0:
                        j += 1
                    elif acc > 0:
                        k -= 1
            
        return result
            
                        