# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        D = ListNode(0)
        D.next = head
        length = 0
        pointer = D
        while pointer.next:
            length += 1
            pointer = pointer.next
        pointer = D
        for i in range(length - n):
            pointer = pointer.next
        pointer.next = pointer.next.next
        return D.next
