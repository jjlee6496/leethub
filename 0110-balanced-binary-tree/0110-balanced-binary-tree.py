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
        def valid(root):
            if not root:
                return 0, True
            l, l_b = valid(root.left)
            r, r_b = valid(root.right)
            
            return 1 + max(l, r), l_b and r_b and abs(l - r) <= 1
        
        return valid(root)[1]