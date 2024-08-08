class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        N, M = len(matrix), len(matrix[0])
        x, y = 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_ind = 0
        res = [matrix[0][0]]
        visited = set()
        visited.add((0, 0))
        for _ in range(N*M-1):
            dx, dy = direction[d_ind]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx, ny) in visited:
                d_ind = (d_ind + 1) % 4
                dx, dy = direction[d_ind]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
            visited.add((nx, ny))
            res.append(matrix[nx][ny])
        return res