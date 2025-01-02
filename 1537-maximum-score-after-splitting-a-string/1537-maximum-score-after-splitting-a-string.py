class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(1, len(s)):
            l, r = s[:i].count('0'), s[i:].count('1')
            print(l, r)
            res = max(res, l + r)
        return res