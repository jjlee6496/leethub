class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """

        return ~n & ((1 << n.bit_length()) - 1) if n else 1