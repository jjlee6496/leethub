# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([root])
        left_bottom = None
        while queue:
            curr = queue.popleft()
            left_bottom = curr.val

            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
        return left_bottom