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
        
        q = deque([(root, 0)])
        while q:
            node, val = q.popleft()
            if not node:
                continue
            val += node.val
                
            if node.left:
                q.append((node.left, val))
            if node.right:
                q.append((node.right, val))

            if not node.left and not node.right:
                if val == targetSum:
                    return True
                else:
                    continue
        return False