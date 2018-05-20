class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.CreateATree(nums)
        return root
        
        
    def CreateATree(self,nums):
        '''
            nums:list[int]
            return type:TreeNode == root
        '''
        if len(nums) == 0:
            return None
        root = TreeNode(max(nums))
        root.left = self.CreateATree(nums[:nums.index(max(nums))])
        root.right = self.CreateATree(nums[nums.index(max(nums)) + 1:])
        
        return root
