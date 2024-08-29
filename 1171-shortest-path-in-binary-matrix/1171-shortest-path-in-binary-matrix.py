class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, 1)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visit = [[0]*n for _ in range(m)]
    
        while q:
            r, c, s = q.popleft()
            visit[r][c] = 1
            if r == m - 1 and c == n - 1:
                return s
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr == m or nc == n or grid[nr][nc] == 1 or visit[nr][nc] == 1:
                    continue
                q.append((nr, nc , s + 1))
                visit[nr][nc] = 1
        return -1