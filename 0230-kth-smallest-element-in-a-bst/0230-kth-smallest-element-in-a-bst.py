# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            if left:
                res.append(left)
            res.append(node.val)
            right = dfs(node.right)
            if right:
                res.append(right)
        dfs(root)
        return res[k - 1]