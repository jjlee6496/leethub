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
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()

            if not node:
                continue
            
            if node.val <= low or node.val >= high:
                return False
            
            stack.append((node.right, node.val, high))
            stack.append((node.left, low, node.val))
        return True