# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)
        result = set([root]) # to track roots
        def dfs(node):
            if not node:
                return None
            
            res = node # None 또는 node.val을 리턴하기 위해
            if node.val in to_delete:
                res = None 
                result.discard(node)
                if node.left: result.add(node.left)
                if node.right: result.add(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res
        dfs(root)
        return list(result)