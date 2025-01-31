class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        island_sizes = {}
        island_id = 2 # 0, 1 제외
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, island_id):
            if min(i, j) < 0 or i >= n or j >= m or grid[i][j] != 1:
                return 0
            grid[i][j] = island_id
            size = 1
            for di, dj in directions:
                size += dfs(i + di, j + dj, island_id)
            return size
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1
        
        if not island_sizes:
            return 1
        
        max_size = max(island_sizes.values())

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    seen = set()
                    new_size = 1
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > 1:
                            island = grid[ni][nj]
                            if island not in seen:
                                new_size += island_sizes[island]
                                seen.add(island)
                    max_size = max(max_size, new_size)
        return max_size


        return max_size
