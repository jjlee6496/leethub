class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def magic(r, c):
            dic = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] in dic or not 1 <= grid[i][j] <= 9:
                        return 0
                    dic.add(grid[i][j])
            # row
            for i in range(r, r+3):
                if sum(grid[r][c:c+3]) != 15:
                    return 0
            # col
            for j in range(c, c+3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15:
                    return 0
            # diag
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2] != 15):
                return 0
            return 1
        M, N = len(grid), len(grid[0])
        if min(M, N) < 3:
            return 0

        res = 0
        for i in range(M - 2):
            for j in range(N - 2):
                res += magic(i, j)
        return res