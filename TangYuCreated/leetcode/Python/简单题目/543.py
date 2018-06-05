# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
    
    def helper(self,root):
        '''
        :type root: TreeNode
        :rtype:(depth of the subtree,the diameter of this subtree)
        '''
        if not root:
            return 0,0
        leftTuple = self.helper(root.left)
        rightTuple = self.helper(root.right)
        diaThroughTheRoot = leftTuple[0] + rightTuple[0]
        depth = max(leftTuple[0],rightTuple[0]) + 1
        diameter = max(diaThroughTheRoot,max(leftTuple[1],rightTuple[1]))
        return depth,diameter
