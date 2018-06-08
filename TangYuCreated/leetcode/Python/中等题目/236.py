# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.findQ = False
        self.findP = False
        self.finish = False
        self.result = None
        self.isAncestor(root,q,p)
        return self.result
        
    def isAncestor(self,root,q,p):
        if root == None:
            return False,False
        if not self.finish:
            ancestorOfQ = False
            ancestorOfP = False
            if root == q:
                ancestorOfQ = True
                self.findQ = True
            elif root == p:
                ancestorOfP = True
                self.findP = True
            if not self.findQ or not self.findP:
                if not self.findQ and not self.findP:
                    left = self.isAncestor(root.left,q,p)
                    right = self.isAncestor(root.right,q,p)
                    ancestorOfQ,ancestorOfP = left[0] or right[0],left[1] or right[1]
                elif not self.findQ:
                    left = self.isAncestor(root.left,q,p)
                    right = self.isAncestor(root.right,q,p)
                    ancestorOfQ = left[0] or right[0]
                elif not self.findP:
                    left = self.isAncestor(root.left,q,p)
                    right = self.isAncestor(root.right,q,p)
                    ancestorOfP = left[1] or right[1]
            if ancestorOfP and ancestorOfQ and not self.finish:
                self.result = root
                self.finish = True
            return ancestorOfQ,ancestorOfP
            
