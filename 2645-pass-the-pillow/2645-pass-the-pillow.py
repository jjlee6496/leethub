class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        ind = 1
        dir = 1
        while time:
            if ind == n:
                dir = -1

            ind += 1*dir

            if ind == 1 and dir == -1:
                dir = 1
            time -= 1
        return ind