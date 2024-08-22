class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        i2, i3, i5 = 0, 0, 0

        for _ in range(1, n):
            next_num = min(
                dp[i2] * 2,
                dp[i3] * 3,
                dp[i5] * 5
            )
            dp.append(next_num)

            if next_num == dp[i2] * 2:
                i2 += 1
            if next_num == dp[i3] * 3:
                i3 += 1
            if next_num == dp[i5] * 5:
                i5 += 1
        return dp[n - 1]