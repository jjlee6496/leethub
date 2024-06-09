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
        def dfs(node, curr):
            if not node:
                return False
            curr += node.val

            if not node.left and not node.right:
                return curr == targetSum
            
            return dfs(node.left, curr) or dfs(node.right, curr)

        return dfs(root, 0)