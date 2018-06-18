# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.result = None
        def helper(fatherNode,node):
            if node:
                nextNode = node.next
                node.next = fatherNode
                helper(node,nextNode)
            else:
                self.result = fatherNode
        helper(None,head)
        return self.result
