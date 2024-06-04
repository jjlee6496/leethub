class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(grid)
        res = [[0]*(N-2) for _ in range(N - 2)]

        for i in range(N-2):
            for j in range(N-2):
                m = 0
                for k in range(3):
                    for l in range(3):
                        m = max(m, grid[i+k][j+l])
                res[i][j] = m
        return res
