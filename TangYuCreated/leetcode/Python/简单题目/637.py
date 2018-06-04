# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return 0
        currentLevel = [root]
        result = []
        while len(currentLevel) > 0:
            currentValue = sum([node.val for node in currentLevel]) / len(currentLevel)
            result.append(currentValue)
            
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
            
        return result
