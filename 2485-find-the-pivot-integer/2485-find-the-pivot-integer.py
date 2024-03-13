class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = (l + r)/2
            leftsum = m*(m + 1)/2
            rightsum = n*(n + 1)/2 - leftsum + m
            if leftsum == rightsum:
                return m
            elif leftsum < rightsum:
                l = m + 1
            else:
                r = m - 1
        return -1