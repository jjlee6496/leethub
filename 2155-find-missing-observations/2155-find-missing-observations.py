class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        sum_miss = (len(rolls) + n)*mean - sum(rolls)
        if sum_miss > 6 * n or sum_miss<0:
            return []
        num, denom = divmod(sum_miss, n)
        if num == 0:
            return []
        res = [num] * n
        for i in range(denom):
            res[i] += 1
        return res