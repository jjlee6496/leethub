class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        curr = [0] * m
        for j in range(n - 2, -1, -1):
            next_col = curr[:]
            for i in range(m):
                curr[i] = 0
                for ni in [i - 1, i, i + 1]:
                    if 0 <= ni < m and grid[ni][j + 1] > grid[i][j]:
                        curr[i] = max(curr[i], next_col[ni] + 1)
        return max(curr)