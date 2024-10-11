class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = 0
        for p in s:
            if p == "[":
                stack += 1
            else:
                if stack > 0:
                    stack -= 1
        return (stack + 1) >> 1