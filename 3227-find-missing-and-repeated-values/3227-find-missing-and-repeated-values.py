class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        res = [0, 0]
        nums = [-1 for i in range(n * n + 1)]
        for g in grid:
            for num in g:
                if nums[num] != -1:
                    res[0] = num
                nums[num] = 0
        for i in range(1, n * n + 1):
            if nums[i] == -1:
                res[1] = i
        return res