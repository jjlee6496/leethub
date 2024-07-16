# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, curr, path):
            if not node:
                return
            
            curr += node.val
            path.append(node.val)

            if not node.left and not node.right and curr == targetSum:
                res.append(path[:])
            else:
                if node.left:
                    dfs(node.left, curr, path)
                if node.right:
                    dfs(node.right, curr, path)
            path.pop()
        
        dfs(root, 0, [])
        return res