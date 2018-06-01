# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        valueInTheSameLevel = [root.val]
        nodesInTheSameLevel = [root]
        
        while nodesInTheSameLevel != []:
            if valueInTheSameLevel != list(reversed(valueInTheSameLevel)):
                return False
            newNodes = []
            newValues = []
            for node in nodesInTheSameLevel:
                if node.left:
                    newNodes.append(node.left)
                    newValues.append(node.left.val)
                else:
                    newValues.append(None)
                if node.right:
                    newNodes.append(node.right)
                    newValues.append(node.right.val)
                else:
                    newValues.append(None)
                    
            nodesInTheSameLevel = newNodes
            valueInTheSameLevel = newValues
        return True
