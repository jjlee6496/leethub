class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        # 각 row의 최소값 2개만 필요
        def get_min_two(r):
            m1, m2 = float('inf'), float('inf')
            idx1, idx2 = -1, -1
            for c in range(N):
                if grid[r][c] <= m1:
                    m1, m2 = grid[r][c], m1
                    idx1, idx2 = c, idx1
                elif grid[r][c] < m2:
                    m2, idx2 = grid[r][c], c
            return [(m1, idx1), (m2, idx2)]
        # 각 row에서 찾아온 최솟값 2개로 업데이트
        # O(N^2), O(1)
        for r in range(1, N):
            min_dp = get_min_two(r-1)
            for c in range(N):
                grid[r][c] += min_dp[0][0] if min_dp[0][1] != c else min_dp[1][0]

        return min(grid[N-1])