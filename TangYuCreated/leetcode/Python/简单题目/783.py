# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.List = []
        self.dfs(root)
        mini = float('inf')
        for i in range(len(self.List) - 1):
            if self.List[i + 1] - self.List[i] < mini:
                mini = self.List[i + 1] - self.List[i]
        return mini
    
    def dfs(self,root):
        if root:
            self.dfs(root.left)
            self.List.append(root.val)
            self.dfs(root.right)
