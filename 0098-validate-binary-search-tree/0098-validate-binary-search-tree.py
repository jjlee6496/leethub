# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, min_val, max_val = stack.pop()
            if node.val <= min_val or node.val >= max_val:
                return False
            if node.left:
                stack.append((node.left, min_val, node.val))
            if node.right:
                stack.append((node.right, node.val, max_val))
        return True