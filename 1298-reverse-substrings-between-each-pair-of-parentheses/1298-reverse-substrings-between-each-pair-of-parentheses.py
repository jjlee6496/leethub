class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                rev = []
                while stack and stack[-1] != '(':
                    rev.append(stack.pop()[::-1])
                stack.pop()
                stack.append(''.join(rev))
            else:
                stack.append(c)
        return ''.join(stack)