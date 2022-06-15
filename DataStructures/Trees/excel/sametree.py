# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and q or p != q:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right,q.right))