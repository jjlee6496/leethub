class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def helper(cnt, paste):
            if cnt == n:
                return 0
            
            if cnt > n:
                return 1000

            if (cnt, paste) in cache:
                return cache[(cnt, paste)]

            res1 = 1 + helper(cnt + paste, paste)
            res2 = 2 + helper(cnt + cnt, cnt)
            cache[(cnt, paste)] = min(res1, res2)
            return cache[(cnt, paste)]
        if n == 1:
            return 0
        return 1 + helper(1, 1)