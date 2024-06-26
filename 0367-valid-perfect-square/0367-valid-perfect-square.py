class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(1, int(math.sqrt(num)+1)):
            if i*i == num:
                return True
        return False