# Definition for singly-linked list.
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
        return pointer1
