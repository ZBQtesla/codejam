# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        self.inverttrees(root)
        return root
    def inverttrees(self,root):
        '''
        return type:None
        
        '''
        root.left,root.right = root.right,root.left
        if root.left != None:
            self.inverttrees(root.left)
        if root.right != None:
            self.inverttrees(root.right)
