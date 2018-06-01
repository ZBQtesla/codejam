# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        nodesInTheSameLevel = [root]
        count = 0
        while len(nodesInTheSameLevel) != 0:
            count += len(nodesInTheSameLevel)
            newNodes = []
            for node in nodesInTheSameLevel:
                if node.left:
                    newNodes.append(node.left)
                if node.right:
                    newNodes.append(node.right)
            nodesInTheSameLevel = newNodes
        return count
