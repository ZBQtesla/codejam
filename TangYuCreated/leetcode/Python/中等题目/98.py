# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValideRoot(float('-inf'),float('inf'),root)
    
    def isValideRoot(self,mini,maxi,root):
        '''
        :type mini:integer
        :type maxi:integer
        :type root:TreeNode
        :return type:bool
        '''
        #connotative condition for this function:None.It can handle null TreeNode
        if root == None:
            return True
        if root.val >= maxi or root.val <= mini:
            return False
        else:
            isValidLeft = self.isValideRoot(mini,root.val,root.left)
            return isValidLeft and self.isValideRoot(root.val,maxi,root.right)
            
