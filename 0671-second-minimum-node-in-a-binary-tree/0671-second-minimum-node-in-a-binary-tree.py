# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.smallest = root.val
        self.res = float('inf')
        def dfs(root):
            if not root:
                return
            if self.smallest < root.val < self.res:
                self.res = root.val

            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return self.res if self.res < float('inf') else -1