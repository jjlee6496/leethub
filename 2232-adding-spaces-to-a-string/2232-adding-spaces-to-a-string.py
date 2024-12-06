class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans = []
        prev = 0
        for ind in spaces:
            ans.append(s[prev:ind])
            ans.append(' ')
            prev = ind
        ans.append(s[prev:])
        return ''.join(ans)