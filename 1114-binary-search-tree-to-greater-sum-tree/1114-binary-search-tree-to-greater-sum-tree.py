# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def dfs(node):
            if not node:
                return None

            if node.right:
                dfs(node.right)

            node.val += self.sum
            self.sum = node.val

            if node.left:
                dfs(node.left)
            return node
        return dfs(root)