# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if root.val == p.val or root.vaclass Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        for i in range(nums.count(val)):
            nums.remove(val)
            length -= 1
        return lengthl == q.val:
                return root
            elif (root.val - q.val) * (root.val - p.val) < 0:
                return root
            elif root.val < q.val:
                root = root.right
            else:
                root = root.left
