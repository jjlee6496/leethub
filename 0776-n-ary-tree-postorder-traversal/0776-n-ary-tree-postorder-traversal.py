"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if not root:
                return
            for c in root.children:
                dfs(c)
            res.append(root.val)
        dfs(root)
        return res