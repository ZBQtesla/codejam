# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        currentLevel = [root]
        nodeList = []
        while currentLevel:
            nodeList.extend(currentLevel)
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        
        nodeList.sort(key = lambda node:node.val)
        currentMax = nodeList[-1].val
        accumulatePre = 0
        accumulateCur = 0
        position = len(nodeList) - 1
        while position >= 0:
            if nodeList[position].val == currentMax:
                accumulateCur += nodeList[position].val
                nodeList[position].val += accumulatePre
            else:
                accumulatePre += accumulateCur
                accumulateCur = nodeList[position].val
                nodeList[position].val += accumulatePre
            position -= 1
        return root
