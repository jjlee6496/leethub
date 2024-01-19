class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix) # symmetric
        for x, y in product(range(1, n), range(n)):
            matrix[x][y] += min(matrix[x-1][max(0, y-1)], matrix[x-1][y], matrix[x-1][min(y+1, n-1)])
        return min(matrix[-1])