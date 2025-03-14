class Solution(object):
    def check(self, candies, t, k):
        cnt = 0
        for candy in candies:
            cnt += candy // t
        if cnt >= k:
            return True
        else:
            return False

    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(candies)
        if s < k:
            return 0

        l, r = 1, s / k
        ans = 0
        while l <= r:
            m = l + (r - l) // 2
            if self.check(candies, m, k):
                ans = max(ans, m)
                l = m + 1
            else:
                r = m - 1
        return ans