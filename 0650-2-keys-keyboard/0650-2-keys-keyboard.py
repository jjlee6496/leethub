class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {}
        def helper(cnt, clip):
            if cnt > n:
                return 1001
            if cnt == n:
                return 0
            if (cnt, clip) in mem:
                return mem[(cnt, clip)]
            res1 = 1 + helper(cnt + clip, clip)
            res2 = 2 + helper(cnt + cnt, cnt)
            mem[(cnt, clip)] = min(res1, res2)
            return mem[(cnt, clip)]
        if n == 1:
            return 0
        return 1 + helper(1, 1)