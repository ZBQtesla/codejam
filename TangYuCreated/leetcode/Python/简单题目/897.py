# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,root):
        '''
        the first return argument is the head and the latter is the tail
        '''
        if not root.left and not root.right:
            return root,root
        elif not root.right:
            leftHead,leftTail = self.helper(root.left)
            
            leftTail.right = root
            root.left = root.right = None
            
            return leftHead,root
        elif not root.left:
            rightHead,rightTail = self.helper(root.right)
            root.right = rightHead

            return root,rightTail
        else:
            leftHead,leftTail = self.helper(root.left)
            rightHead,rightTail = self.helper(root.right)
            
            leftTail.right = root
            root.left = None
            root.right = rightHead
            
            return leftHead,rightTail
        
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[0]
