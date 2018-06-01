# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []
        def bfs(root,level):
            if root != None:
                if len(result) < level + 1:
                    result.append([])
                result[level].append(root.val)
                bfs(root.left,level + 1)
                bfs(root.right,level + 1)
        bfs(root,0)
        return result
