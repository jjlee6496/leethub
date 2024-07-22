# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans = []
        def dfs(node, cnt):
            if not node.left and not node.right:
                ans.append(cnt)
                return
            
            if node.left:
                dfs(node.left, cnt+1)
            if node.right:
                dfs(node.right, cnt+1)

        dfs(root, 1)
        return max(ans)