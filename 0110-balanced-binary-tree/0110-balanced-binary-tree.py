# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        def valid(root):
            if not root:
                return 0
            l = valid(root.left)
            if l == -1:
                return -1
            r = valid(root.right)
            if r == -1:
                return -1
            if abs(l - r) > 1:
                return -1
            return 1 + max(l, r)
        return valid(root) != -1