class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        t1 = ''
        for c in s:
            t1 += str(ord(c) - ord('a') + 1)
        
        while k:
            res = 0
            for c in t1:
                res += int(c)
            k -= 1
            if k > 0:
                t1 = str(res)
        return res