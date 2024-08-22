class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        
        ugly = sorted(2**a * 3 ** b * 5** c for a in range(32) for b in range(20) for c in range(14))
        return ugly[n - 1]