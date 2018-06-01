# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        
        def rightSideViewHelp(level,root):
            if root != None:
                if len(result) < level + 1:
                    result.append(root.val)
                rightSideViewHelp(level + 1,root.right)
                rightSideViewHelp(level + 1,root.left)
                
        rightSideViewHelp(0,root)
        return result
        
            
