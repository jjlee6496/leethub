# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def minValNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = minValNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root