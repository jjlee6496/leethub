class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        dic = set()
        for a in range(int(math.sqrt(c))+1):
            dic.add(a*a)

        for b in range(int(math.sqrt(c))+1):
            if c - b*b in dic:
                return True
        return False