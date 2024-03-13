class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, n+1):
            if sum([x for x in range(i+1, n+1)])==i*(i-1)/2:
                return i
        return -1