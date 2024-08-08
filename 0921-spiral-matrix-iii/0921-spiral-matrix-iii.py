class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        d_ind = 0
        r, c = rStart, cStart
        step = 1
        while len(res) < rows*cols:
            for _ in range(2): # step은 2번마다 바뀜
                dr, dc = direction[d_ind]
                for _ in range(step):
                    if 0<=r<rows and 0<=c<cols:
                        res.append([r, c])
                    r, c = r + dr, c + dc
                d_ind = (d_ind + 1) % 4
            step += 1
        return res
