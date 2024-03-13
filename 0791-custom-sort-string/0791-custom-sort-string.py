class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        ans = ''.join(sorted(s, key=lambda x: order.index(x) if x in order else -1))
        return ans