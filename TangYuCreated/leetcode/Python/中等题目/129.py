# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root,0)
        return self.result
    def dfs(self,root,number):
        if root:
            already = number * 10 + root.val
            isleaf = not root.left and not root.right
            if isleaf:
                self.result += already
            else:
                self.dfs(root.left,already)
                self.dfs(root.right,already)
