class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def dfs(ind, path):
            res.append(path[:])

            for i in range(ind, len(nums)):
                if i > ind and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res