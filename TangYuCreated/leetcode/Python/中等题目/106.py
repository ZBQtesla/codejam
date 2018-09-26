# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            rootValue = postorder[-1]
            root = TreeNode(rootValue)
            position = inorder.index(rootValue)
            root.left = self.buildTree(inorder[:position],postorder[:position])
            root.right = self.buildTree(inorder[position + 1:],postorder[position:-1])
            return root
