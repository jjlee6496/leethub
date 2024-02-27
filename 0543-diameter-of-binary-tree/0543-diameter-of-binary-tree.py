# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update the maximum diameter
            nonlocal diameter
            diameter = max(diameter, left_depth + right_depth)

            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)

        diameter = 0
        depth(root)
        return diameter