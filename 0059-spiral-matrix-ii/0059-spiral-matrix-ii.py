class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        x, y = 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_ind = 0
        res[0][0] = 1
        for i in range(2, n**2+1):
            dx, dy = direction[d_ind]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or res[nx][ny] != 0:
                d_ind = (d_ind + 1) % 4
                dx, dy = direction[d_ind]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
            res[nx][ny] = i
        return res