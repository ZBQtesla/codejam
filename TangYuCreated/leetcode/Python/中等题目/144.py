# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        result = [root.val]
        if root.left != None:
            result.extend(self.preorderTraversal(root.left))
        if root.right != None:
            result.extend(self.preorderTraversal(root.right))
        return result
