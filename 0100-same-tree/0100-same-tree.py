# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.traverse(p)==self.traverse(q)
        
    def traverse(self, node):
        result = []
        if not node:
            result.append(None)
        if node:
            result.append(node.val)
            result.extend(self.traverse(node.left))
            result.extend(self.traverse(node.right))

        return result