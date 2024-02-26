# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.traverse(root)
    
    def traverse(self, node):
        result = []
        if node:
            result.extend(self.traverse(node.left))
            result.append(node.val)
            result.extend(self.traverse(node.right))
        return result