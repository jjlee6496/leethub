class Solution(object):
    dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        prev = 0
        for c in reversed(s):
            curr = self.dic[c]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr
        return res