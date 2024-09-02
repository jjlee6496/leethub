class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)
        n = len(chalk)
        ind = 0
        while k > 0:
            k -= chalk[ind]
            ind = (ind + 1) % n
        return ind if k == 0 else (ind - 1 + n) % n