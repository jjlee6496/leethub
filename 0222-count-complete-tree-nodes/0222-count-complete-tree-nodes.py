# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque([root])
        cnt = 0
        while q:
            node = q.popleft()
            if node:
                cnt += 1
            if node and node.left:
                q.append(node.left)

            if node and node.right:
                q.append(node.right)

        return cnt