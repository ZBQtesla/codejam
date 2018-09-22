# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.sameValue(root)[0] - 1
        
    def sameValue(self,root):
        '''
        return value:(the longestUnivaluePath in this subtree,the longest Univalue Path from this root)
        '''
        if not root:
            return 0,0
        else:
            leftPara,rightPara = self.sameValue(root.left),self.sameValue(root.right)
            pathLen = 1
            leftPath = rightPath = 1
            if root.left and root.left.val == root.val:
                pathLen += leftPara[1]
                leftPath += leftPara[1]
            if root.right and root.right.val == root.val:
                pathLen += rightPara[1]
                rightPath += rightPara[1]
            
            return max(leftPara[0],rightPara[0],pathLen),max(leftPath,rightPath)
