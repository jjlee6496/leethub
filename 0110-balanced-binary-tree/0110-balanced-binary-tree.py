# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0
            
            l, r = check(node.left), check(node.right)

            if l < 0 or r < 0 or abs(l - r) > 1:
                return -1
            
            return max(l, r) + 1

        return check(root) >= 0