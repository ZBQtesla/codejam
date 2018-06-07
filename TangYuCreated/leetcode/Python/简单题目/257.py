# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            self.helper(root.left,str(root.val))
        if root.right:
            self.helper(root.right,str(root.val))
        return self.result
    
    def helper(self,root,string):
        if not root.left and not root.right:
            self.result.append(string + '->' + str(root.val))
    
        else:
            if root.left:
                self.helper(root.left,string + '->'+str(root.val))
            
            if root.right:
                self.helper(root.right,string + '->' + str(root.val))
        
