class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k:
            return 0

        l, r = 1, max(candies)
        while l < r:
            m = l + (r - l + 1) // 2
            res = sum(pile // m for pile in candies)
            if res >= k:
                l = m
            else:
                r = m - 1
        return l