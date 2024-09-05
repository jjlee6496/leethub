class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])
        def dfs(i, j):
            if min(i, j) < 0 or i == m or j == n or grid2[i][j] == 0:
                return True
            
            grid2[i][j] = 0 # 방문
            res = grid1[i][j] == 1
            res &= dfs(i - 1, j)
            res &= dfs(i + 1, j)
            res &= dfs(i, j - 1)
            res &= dfs(i, j + 1)
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    res += 1
        return res
            