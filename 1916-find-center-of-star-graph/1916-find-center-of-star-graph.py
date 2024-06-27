class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        u1, u2 = edges[0][0], edges[0][1]
        return u1 if u1 in [edges[1][0], edges[1][1]] else u2