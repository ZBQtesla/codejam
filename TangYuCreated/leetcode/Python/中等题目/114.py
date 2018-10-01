# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,root):
        if root:
            rootLeft,rootRight = root.left,root.right
            self.last.right = root
            self.last = self.last.right
            self.helper(rootLeft)
            self.helper(rootRight)
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.last = root
        rootLeft,rootRight = root.left,root.right
        self.helper(rootLeft)
        self.helper(rootRight)
        while root:
            root.left = None
            root = root.right
