class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = 0
        res = 0
        for p in s:
            if p == '(':
                stack += 1
            else:
                if stack:
                    stack -= 1
                else:
                    res += 1
        return stack + res