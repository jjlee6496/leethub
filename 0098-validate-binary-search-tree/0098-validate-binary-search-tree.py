# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, low=float('-inf'), high=float('inf')):
            if not root:
                return True
            
            if low >= root.val or high <=  root.val:
                return False
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
        
        return dfs(root)