class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n - 2, -1, -1):
            for i in range(m):
                for ni in [i - 1, i, i + 1]:
                    if 0 <= ni < m and grid[ni][j + 1] > grid[i][j]:
                        dp[i][j] = max(dp[i][j], dp[ni][j + 1] + 1)
        return max(dp[i][0] for i in range(m))