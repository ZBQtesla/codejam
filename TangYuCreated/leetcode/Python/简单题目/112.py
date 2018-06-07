# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        isleaf = not root.left and not root.right
        if isleaf:
            if sum == root.val:
                return True
            else:
                return False
        if not isleaf:
            return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)
