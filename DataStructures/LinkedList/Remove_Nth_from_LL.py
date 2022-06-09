# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy= ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next

        #delete
        left.next = left.next.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    s.removeNthFromEnd([1,2,3,4,5], 2)