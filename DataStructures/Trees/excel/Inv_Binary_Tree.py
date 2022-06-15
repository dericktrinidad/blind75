class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        left, right = root.left, root.right

        mem = left
        left = right
        right = mem

        self.invertTree(left)
        self.invertTree(right)

        return root