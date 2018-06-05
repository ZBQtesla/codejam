# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root,False)
    
    def helper(self,node,isleftchild):
        if not node:
            return 0
        isLeaf = not node.left and not node.right
        if isLeaf and isleftchild:
            return node.val
        else:
            return self.helper(node.left,True) + self.helper(node.right,False)
