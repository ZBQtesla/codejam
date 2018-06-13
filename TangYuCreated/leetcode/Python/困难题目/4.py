class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1  = len(nums1)
        length2 = len(nums2)
        
        while length1 > 2 and length2 > 2:
            isodd1 = not length1 % 2 == 0
            isodd2 = not length2 % 2 == 0
            if isodd1 :
                middlenum1 = nums1[(length1 - 1)// 2]
            else:
                middlenum1 = (nums1[(length1 - 1) // 2] + nums1[(length1 - 1) // 2 + 1]) / 2
            
            if isodd2:
                middlenum2 = nums2[(length2 - 1) // 2]
            else:
                middlenum2 = (nums2[(length2 - 1) // 2] + nums2[(length2 - 1) // 2 + 1]) / 2            
            #find the median of both lists
            
            toBeDeleted1 = length1 // 2 if isodd1 else length1 // 2 - 1
            toBeDeleted2 = length2 // 2 if isodd2 else length2 // 2 - 1
            toBeDeleted = min(toBeDeleted1,toBeDeleted2)
            
            if middlenum1 > middlenum2:
                nums1 = nums1[:-toBeDeleted]
                nums2 = nums2[toBeDeleted:]
            else:
                nums1 = nums1[toBeDeleted:]
                nums2 = nums2[:-toBeDeleted]
                
            length1 -= toBeDeleted
            length2 -= toBeDeleted

        if length1 <= 2:
            for val in nums1:
                nums2.insert(self.searchInsert(nums2,val),val)
                length2 += 1
            if length2 % 2 != 0:
                return nums2[(length2 - 1) // 2]
            else:
                return (nums2[(length2 - 1) // 2] + nums2[(length2 - 1) // 2 + 1]) / 2
        else:
            for val in nums2:
                nums1.insert(self.searchInsert(nums1,val),val)
                length1 += 1
            if length1 % 2 != 0 :
                return nums1[(length1 - 1 )// 2]
            else:
                return (nums1[(length1 - 1 )// 2] + nums1[(length1 - 1 ) // 2 + 1]) / 2
                
    
    
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
        elif target >= nums[-1]:
            return length
        
        #assume that this nums is long,and the position of the insertion is within the list
        left = 0
        right = length - 1
        while True:
            middle = (left + right) // 2
            if nums[middle] <= target <= nums[middle + 1]:
                return middle + 1
            elif target <= nums[middle]:
                right = middle
            else:
                left = middle + 1
