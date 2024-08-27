# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return 0
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            return 1
        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)
        return left or right