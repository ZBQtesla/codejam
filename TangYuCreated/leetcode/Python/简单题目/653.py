class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        currentLevel = [root]
        listValue = []
        while len(currentLevel):
            listValue.extend([node.val for node in currentLevel])
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        listValue.sort()
        begin = 0
        end = len(listValue) - 1
        while begin != end:
            tempResult = listValue[begin] + listValue[end]
            if tempResult < k:
                begin += 1
            elif tempResult > k:
                end -= 1
            else:
                return True
        return False
                
