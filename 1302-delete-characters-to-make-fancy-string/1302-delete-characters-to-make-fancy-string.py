class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = 1
        res = []
        for c in s:
            if res and res[-1] == c:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res.append(c)
        return ''.join(res)