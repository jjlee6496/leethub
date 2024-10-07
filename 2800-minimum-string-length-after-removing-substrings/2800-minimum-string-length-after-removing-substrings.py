class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s.find('AB') >= 0 or s.find('CD') >= 0:
            s = s.replace('AB', '')
            s = s.replace('CD', '')
        return len(s)