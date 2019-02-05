class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        if l1.val < l2.val:
            start = ListNode(l1.val)
            l1 = l1.next
        else:
            start = ListNode(l2.val)
            l2 = l2.next
        p = start
        while l1 and l2:
            if l1.val<l2.val:
                new = ListNode(l1.val)
                p.next = new
                p = p.next
                l1 = l1.next
            else :
                new = ListNode(l2.val)
                p.next = new
                p = p.next
                l2 = l2.next
        while l1:
            new = ListNode(l1.val)
            p.next = new
            p = p.next
            l1 = l1.next
        while l2:
            new = ListNode(l2.val)
            p.next = new
            p = p.next
            l2 = l2.next
        return start
