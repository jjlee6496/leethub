class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('0b'+''.join(['0' if b=='1' else '1' for b in bin(num)[2:]]), 2)