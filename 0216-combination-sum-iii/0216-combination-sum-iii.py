class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(start, curr, path):
            if curr == n and len(path) == k:
                res.append(path)
                return

            for i in range(start, 10):
                if curr + i > n:
                    break
                dfs(i + 1, curr + i, path + [i])
        dfs(1, 0, [])
        return res
