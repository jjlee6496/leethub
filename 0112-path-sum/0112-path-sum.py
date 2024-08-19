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
        def backtrack(root, curr):
            if not root:
                return False
            
            curr += root.val

            if not root.left and not root.right:
                return curr == targetSum
            
            return backtrack(root.left, curr) or backtrack(root.right, curr)
        return backtrack(root, 0)