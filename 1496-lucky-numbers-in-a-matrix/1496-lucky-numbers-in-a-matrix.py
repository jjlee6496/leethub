class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        maxs = []

        for m in zip(*matrix):
            maxs.append(max(m))
    
        for i in range(len(matrix)):
            a = min(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == maxs[j] and a == matrix[i][j]:
                    ans.append(matrix[i][j])
        return ans

