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
        List = []
        if not head:
            return []
        while head.next != None:
            List.append(head)
            head = head.next
        List.append(head)
        for i in range(len(List) - 1,0,-1):
            List[i].next = List[i - 1]
        List[0].next = None
        return List[-1]
