from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        unbalance_count = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                elif node.left and not node.right:
                    q.append(node.left)
                    unbalance_count += 1
                elif node.right and not node.left:
                    q.append(node.right)
                    unbalance_count += 1
        return unbalance_count > 1

