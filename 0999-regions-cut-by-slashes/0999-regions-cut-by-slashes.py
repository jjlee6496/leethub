class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        grid2 = [[0] * (3*N) for _ in range(3*N)]
        for i in range(N):
            for j in range(N):
                row = i * 3
                col = j * 3
                if grid[i][j] == '/':
                    grid2[row][col+2] = 1
                    grid2[row+1][col+1] = 1
                    grid2[row+2][col] = 1
                elif grid[i][j] == '\\':
                    grid2[row][col] = 1
                    grid2[row+1][col+1] = 1
                    grid2[row+2][col+2] = 1
        def dfs(r, c):
            if r<0 or r==3*N or c<0 or c==3*N or grid2[r][c]:
                return
            grid2[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        res = 0
        for i in range(N*3):
            for j in range(N*3):
                if grid2[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res
                    