class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        cnt = {}
        res = 0
        for x in s:
            cnt[x] = cnt.get(x, 0) + 1
        odd = 0
        if len(cnt.keys()) == 1:
            return len(s)
        for k, v in cnt.items():
            if v % 2:
                res += v - 1
                odd = 1
            else:
                res += v
        return res if not odd else res + odd

