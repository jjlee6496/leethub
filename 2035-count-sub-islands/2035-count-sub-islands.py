class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid2[i][j] == 1:
                grid2[i][j] = 0
                return grid1[i][j] & dfs(i+1, j) & dfs(i-1, j) & dfs(i, j+1) & dfs(i, j-1)
            return 1

        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid2[i][j])