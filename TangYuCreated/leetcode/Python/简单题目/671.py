# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.min1 = float('inf')
        self.min2 = float('inf')
        self.helper(root)
        return self.min2 if self.min2 != float('inf') else -1
    
    def helper(self,root): 
        if root.val < self.min1:
            self.min1,self.min2 = root.val,self.min1
        elif self.min1 < root.val < self.min2:
            self.min2 = root.val
        
        isleaf = not bool(root.left)
        if not isleaf:
            self.helper(root.left)
            self.helper(root.right)
