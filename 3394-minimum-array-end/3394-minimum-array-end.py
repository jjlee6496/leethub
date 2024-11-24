class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        res = x
        i_x = 1
        i_n = 1
        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res |= i_x
                i_n <<= 1
            i_x <<= 1
        return res
