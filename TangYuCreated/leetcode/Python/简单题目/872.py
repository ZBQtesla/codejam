# Definition for a binary tree node.
# class# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer1 = pointer2 = head
        
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            
            pointer2 = pointer2.next.next
        return pointer1 TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.helper(root1) == self.helper(root2)
        
    def helper(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            return self.helper(root.left) + self.helper(root.right)
