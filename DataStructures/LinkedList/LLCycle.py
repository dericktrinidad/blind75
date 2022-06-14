# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head

        while head and head.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
