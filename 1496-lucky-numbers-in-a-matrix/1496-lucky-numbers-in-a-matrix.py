class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        maxs = [max(x) for x in zip(*matrix)]

        for i in range(len(matrix)):
            a = min(matrix[i])
            if a in maxs:
                return [a]
        return []