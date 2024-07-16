# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def lca(node):
            # 타겟 노드 혹은 리프노드일 경우
            if not node or node.val in (startValue, destValue):
                return node

            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        def find(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True
            
            path.append('L')
            if find(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if find(node.right, target, path):
                return True
            path.pop()
            return False
        lca_node = lca(root)
        start_path, dest_path = [], []
        find(lca_node, startValue, start_path)
        find(lca_node, destValue, dest_path)
        return 'U'*len(start_path) + ''.join(dest_path)