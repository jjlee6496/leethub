class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if min(r, c) < 0 or r == m or c == n or grid2[r][c] == 0:
                return True
            is_sub = grid1[r][c] == 1
            grid2[r][c] = 0
            for dr, dc in directions:
                is_sub &= dfs(r + dr, c + dc)
            return is_sub
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    res += 1                    
        return res