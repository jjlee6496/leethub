# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = defaultdict(int) # hash map
        self.odd = 0
        def dfs(curr):
            if not curr:
                return 0
            
            count[curr.val] += 1
            odd_change = 1 if count[curr.val] % 2 == 1 else -1
            self.odd += odd_change
            if not curr.left and not curr.right:
                res = 1 if self.odd <= 1 else 0
            else:
                res = dfs(curr.left)+dfs(curr.right)
            self.odd -= odd_change
            count[curr.val] -= 1
            return res
        return dfs(root)