class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        def dfs(ind, subset):
            res.append(subset[:])
            for i in range(ind, len(nums)):
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
        dfs(0, [])
        return res
