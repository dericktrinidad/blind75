class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while head:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev