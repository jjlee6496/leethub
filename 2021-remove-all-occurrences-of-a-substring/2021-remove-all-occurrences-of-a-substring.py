class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        pos = s.find(part)
        while pos != -1:
            s = s[0:pos] + s[pos+len(part):]
            pos = s.find(part)

        return s