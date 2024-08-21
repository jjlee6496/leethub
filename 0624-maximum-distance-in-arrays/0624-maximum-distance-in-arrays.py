class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res = 0
        maxd = arrays[0][-1]
        mind = arrays[0][0]
        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - mind, maxd - arrays[i][0])
            maxd = max(maxd, arrays[i][-1])
            mind = min(mind, arrays[i][0])
        return res