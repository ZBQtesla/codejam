# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        isleaf = not root.left and not root.right
        if isleaf:
            if root.val == sum:
                return [[sum]]
            else:
                return []
        else:
            leftPaths = self.pathSum(root.left,sum - root.val)
            rightPaths = self.pathSum(root.right,sum - root.val)
            if leftPaths:
                result.extend([root.val] + path for path in leftPaths)
            if rightPaths:
                result.extend([root.val] + path for path in rightPaths)
        return result
