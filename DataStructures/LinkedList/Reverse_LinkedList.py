class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution1:
    #ITERATIVE
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

class Solution2:
    #RECURSIVE
    def reverseList(self, head):
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

class tryme:
    def reverseList(self, head):
        prev, curr = None, head

        while head:
            nxt = head.next
            head.next = prev
            prev = curr
            curr = nxt

        return prev
if __name__ == '__main__':
    s1 = Solution1()
    s2 = Solution2()
    print(s1.reverseList(ListNode([1,2,3,4,5])))