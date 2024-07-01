class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x
        if not x:
            return 0
        while l <= r:
            mid = (l + r) // 2
            mul = mid * mid
            if mul == x:
                return mid
            elif mul < x:
                l = mid + 1
            else:
                r = mid - 1
        return mid - 1 if mul > x else mid