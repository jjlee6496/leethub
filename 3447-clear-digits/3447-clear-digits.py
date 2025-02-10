class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(s[i])
            else:
                res.pop()
        return ''.join(res)

