class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        n = start ^ goal
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res