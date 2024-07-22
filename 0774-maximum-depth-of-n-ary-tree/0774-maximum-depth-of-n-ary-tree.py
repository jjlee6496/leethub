"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        q = []
        depth = 0
        if root:
            q.append((root, 1))
        
        for node, level in q:
            depth = level
            q.extend([(child, level+1) for child in node.children])
        return depth