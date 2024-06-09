class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0] * k
        temp = 0
        res = 0
        dp[0] = 1
        for num in nums:
            temp = (temp + num) % k
            if dp[temp]:
                res += dp[temp]
            
            dp[temp] += 1
        return res
