# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root])
        even = True
        while queue:
            prev = 0 if even else 10**6 + 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if even and (node.val <= prev or node.val%2==0):
                    return False

                elif not even and (node.val >= prev or node.val%2):
                    return False

                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                prev = node.val
            even = not even    

        return True
            
