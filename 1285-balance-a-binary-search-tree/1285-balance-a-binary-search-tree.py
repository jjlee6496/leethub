# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = deque([root])
        l = []
        while q:
            node = q.popleft()
            l.append(node.val if node else None)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


        l.sort()

        def to_bst(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])

            root.left = to_bst(arr[:mid])
            root.right = to_bst(arr[mid+1:])
            return root
        res = to_bst(l)
        return res
