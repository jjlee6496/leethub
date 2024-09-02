class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m * n < len(original):
            return []
        res = [[0]*n for _ in range(m)]
        ind = 0
        for i in range(m):
            for j in range(n):
                if ind == len(original):
                    return []
                res[i][j] = original[ind]
                ind += 1
        return res