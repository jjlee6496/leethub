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
                return 0, True
            
            l, l_check = check(node.left)
            r, r_check = check(node.right)

            curr_height = 1 + max(l, r)
            curr_check = l_check and r_check and abs(l-r) <= 1
            return curr_height, curr_check
        
        _, res = check(root)
        return res