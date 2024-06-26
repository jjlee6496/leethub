class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(math.sqrt(c))+1
        while left <= right:
            target = left*left + right*right
            if target == c:
                return True
            elif target < c:
                left += 1
            else:
                right -= 1
        return False
