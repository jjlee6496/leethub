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
        stack = []
        if root:
            stack.append(root)
            while stack:
                node = stack.pop()
                res.append(node.val)
                for c in node.children:
                    stack.append(c)
        return res[::-1]