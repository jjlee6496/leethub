class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        mem = {}
        def move(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            if min(i, j) < 0 or i >= m or j >= n:
                return 0
            max_steps = 0
            if i + 1 < m and j + 1 < n and grid[i + 1][j + 1] > grid[i][j]:
                max_steps = max(max_steps, move(i + 1, j + 1))
            if i < m and j + 1 < n and grid[i][j + 1] > grid[i][j]:
                max_steps = max(max_steps, move(i, j + 1))
            if 0 <= i - 1 and j + 1 < n and grid[i - 1][j + 1] > grid[i][j]:
                max_steps = max(max_steps, move(i - 1, j + 1))
            
            mem[(i, j)] = max_steps + 1
            return max_steps + 1
        res = 0
        for i in range(m):
            res = max(res, move(i, 0))
        return res - 1