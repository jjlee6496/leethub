class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit = [c for c in s if c.isdigit()]
        alpha = [c for c in s if c.isalpha()]
        a, b = len(digit), len(alpha)
        if abs(a - b) > 1:
            return ""
        if a > b:
            return ''.join(x+y for x, y in zip(digit, alpha)) + digit[-1]
        elif a < b:
            return ''.join(x+y for x, y in zip(alpha, digit)) + alpha[-1]
        else:
            return ''.join(x+y for x, y in zip(digit, alpha))