# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.helper(root)
        return self.result
    def helper(self,root):
        if root:
            self.helper(root.left)
            self.result.append(root.val)
            self.helper(root.right)
