# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        isReverse = False
        result = []
        currentLevel = [root]
        while currentLevel:
            if isReverse:
                result.append(list(reversed([node.val for node in currentLevel])))
                isReverse = False
            else:
                result.append([node.val for node in currentLevel])
                isReverse = True
            
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result
