# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mini = float('inf')
        self.List = []
        self.helper(root)
        for i in range(len(self.List) - 1):
            dif = self.List[i + 1] - self.List[i]
            mini = min(dif,mini)
        return mini
    
    def helper(self,root):
        if root:
            self.helper(root.left)
            self.List.append(root.val)
            self.helper(root.right)
