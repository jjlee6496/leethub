class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def helper(cnt, clip):
            if cnt > n:
                return 1001
            if cnt == n:
                return 0
            res1 = 1 + helper(cnt + clip, clip)
            res2 = 2 + helper(cnt + cnt, cnt)
            return min(res1, res2)
        if n == 1:
            return 0
        return 1 + helper(1, 1)