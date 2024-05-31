class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(ind, path):
            if tuple(sorted(path[:])) not in res:
                res.append(tuple(sorted(path[:])))
            for i in range(ind, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res