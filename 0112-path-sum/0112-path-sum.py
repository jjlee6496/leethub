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
            return False
        q = deque([(root, root.val)])
        while q:
            node, val = q.popleft()
            if not node.left and not node.right and val==targetSum:
                return True
            if node.left:
                q.append((node.left, node.left.val + val))
            if node.right:
                q.append((node.right, node.right.val + val))
        return False
        