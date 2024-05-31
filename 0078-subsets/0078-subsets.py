class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(ind, path):
            res.append(path[:])
            
            for i in range(ind, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res