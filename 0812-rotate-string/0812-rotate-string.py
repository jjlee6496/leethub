class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(goal)
        if len(s) > n:
            return False
        s = s * 2
        for i in range(len(s) - n):
            if s[i:i+n] == goal:
                return True
        return False