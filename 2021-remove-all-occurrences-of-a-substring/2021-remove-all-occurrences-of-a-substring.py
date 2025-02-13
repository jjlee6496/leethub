class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack = []
        n = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= n:
                while ''.join(stack[-n:]) == part:
                    for _ in range(n):
                        stack.pop()
        return ''.join(stack)