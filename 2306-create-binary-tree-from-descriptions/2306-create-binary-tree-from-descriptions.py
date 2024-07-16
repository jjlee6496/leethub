# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """ 
        dic = {}
        children = set()
        for p, c, left in descriptions:
            if p not in dic:
                dic[p] = TreeNode(p)
            if c not in dic:
                dic[c] = TreeNode(c)
            if left:
                dic[p].left = dic[c]
            else:
                dic[p].right = dic[c]
            children.add(c)
            
        for k in dic.keys():
            if k in children:
                continue
            root = dic[k]
            break
        
        return root
                
                            
            
            
            