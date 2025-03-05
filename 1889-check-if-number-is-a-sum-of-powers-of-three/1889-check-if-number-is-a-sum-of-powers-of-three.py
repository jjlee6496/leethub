class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 14 # log_3 10^7 = 14.6xx
        while x >= 0:
            if n >= 3 ** x:
                n -= 3 ** x
            x -= 1
        return n == 0

