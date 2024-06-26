class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        left, right = 1, int(math.sqrt(num))+1
        while left <= right:

            mid = (right + left) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False