class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        last = days[-1]
        dp = [0] * (last + 1)
        travel = set(days)
        for d in range(1, last + 1):
            dp[d] = dp[d - 1]
            if d in travel:
                dp[d] = min(
                    costs[0] + dp[max(0, d - 1)],
                    costs[1] + dp[max(0, d - 7)],
                    costs[2] + dp[max(0, d - 30)],
                )
        return dp[-1]
