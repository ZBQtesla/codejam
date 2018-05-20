# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #connotative condition here:None
        #root can be anything,including None
        if root == None:
            return None
        elif root.val == 1:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
        else:   #root.val == 0
            if self.isBad(root):
                return None
            else:
                root.left = self.pruneTree(root.left)
                root.right = self.pruneTree(root.right)
        return root
                
    def isBad(self,root):
        '''
            :type root: TreeNode
            :rtype: bool
        '''
        #connotative condition:None.
        #root can be None or anything else
        if root == None:
            return True
        elif root.val == 1:
            return False
        elif root.val == 0:
            return True and self.isBad(root.left) and self.isBad(root.right)
