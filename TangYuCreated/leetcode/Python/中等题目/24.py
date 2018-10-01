# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif not head.next:
            return head
        previous = ListNode(0)
        previous.next = head
        Head = head.next
        while previous.next and previous.next.next:
            first = previous.next
            second = previous.next.next
            third = previous.next.next.next
            
            previous.next = second
            previous.next.next = first
            previous.next.next.next = third
            previous = first
        return Head
