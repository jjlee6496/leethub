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
        self.res = None
        self.k = k
        def dfs(node):
            if not node or self.res:
                return
            
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.right)
        dfs(root)
        return self.res