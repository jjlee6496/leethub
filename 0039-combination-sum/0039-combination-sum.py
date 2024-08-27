class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target+1)]
        dp[0] = [[]]

        for num in candidates:
            for i in range(num, target + 1):
                for comb in dp[i - num]:
                    dp[i].append(comb + [num])
        return dp[target]