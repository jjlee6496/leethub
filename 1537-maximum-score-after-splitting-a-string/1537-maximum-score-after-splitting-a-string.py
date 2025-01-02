class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = s[:1].count('0') + s[1:].count('1')
        max_s = curr
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                curr += 1
            else:
                curr -= 1
            if curr > max_s:
                max_s = curr

        return max_s