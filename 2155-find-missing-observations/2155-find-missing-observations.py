class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total = mean * (n + m)

        miss = total - sum(rolls)
        if miss < n or miss > 6 * n:
            return []
        q, d = divmod(miss, n)
        return [q + 1] * d + [q] * (n - d)