class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, n+1):
            if sum([x for x in range(1, i+1)]) == sum([x for x in range(i, n+1)]):
                return i
        return -1