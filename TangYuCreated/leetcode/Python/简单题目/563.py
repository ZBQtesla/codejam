# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def helper(root):  #used to calculate the summation and update the self.result
            if not root:
                return 0
            leftSum = helper(root.left)
            rightSum = helper(root.right)
            self.result += abs(leftSum - rightSum)
            return leftSum + rightSum + root.val
        helper(root)
        return self.result
