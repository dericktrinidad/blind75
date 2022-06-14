class ListNode:
    def __init__(self, val = 0, head = None):
        self.val = val
        self.head = head

class Solution:
    def mergeTwoLL(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                tail.next = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
