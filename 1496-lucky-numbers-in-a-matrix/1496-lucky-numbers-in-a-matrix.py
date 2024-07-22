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
            if a in maxs:
                return [a]
        return []