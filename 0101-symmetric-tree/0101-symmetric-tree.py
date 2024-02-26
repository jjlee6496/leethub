# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse1(root.left) == self.traverse2(root.right)
    
    def traverse1(self, node):
        if not node:
            return [None]
        
        return [node.val] + self.traverse1(node.left) + self.traverse1(node.right)
    
    def traverse2(self, node):
        if not node:
            return [None]
        
        return [node.val] + self.traverse2(node.right) + self.traverse2(node.left)