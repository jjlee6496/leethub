class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = (1 << num.bit_length()) - 1 # 1의 보수이므로 길이만큼 1을 채운 수를 구함
        return ~num & mask # 토글을 거꾸로 한 것 -> 보수 구해짐