class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums1)):
            posin2 = nums2.index(nums1[i])
            state = True
            for j in nums2[posin2:]:
                if j > nums1[i]:
                    nums1[i] = j
                    state = False
                    break
            if state == True:
                nums1[i] = -1
        return nums1
