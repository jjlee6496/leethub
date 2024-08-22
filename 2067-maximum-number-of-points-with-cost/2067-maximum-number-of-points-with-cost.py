class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dp = points[-1]
        m, n = len(points), len(points[0])
        for i in range(m - 2, -1, -1):
            left = [0] * n
            right = [0] * n

            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(left[j-1] - 1, dp[j])
            
            right[-1] = dp[-1]
            for j in range(n-2, -1, -1):
                right[j] = max(right[j+1] - 1, dp[j])
            
            for j in range(n):
                dp[j] = points[i][j] + max(left[j], right[j])
        return max(dp)
