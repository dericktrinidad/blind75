class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def validate(node, left, right):
            if not node:
                return True
            if node.val < right and node.val > left:
                return False
            return (validate(node.left, left, node.val) and
                    validate(node.right, node.val, right))
        return(validate(root, float("-inf"), float("inf")))