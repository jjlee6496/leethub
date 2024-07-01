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
        left = root
        right = root
        lh = 0
        rh = 0
        if not root:
            return 0

        while left:
            lh += 1
            left = left.left

        while right:
            rh+= 1
            right = right.right
        
        if lh == rh:
            return int(math.pow(2, lh)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)