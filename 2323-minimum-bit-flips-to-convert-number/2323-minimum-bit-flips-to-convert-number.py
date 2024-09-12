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
            n = n & (n - 1)
            res += 1
        return res