class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def dfs(start, curr, path):
            if curr == target:
                res.append(path[:])
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                if candidates[i] + curr > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, candidates[i] + curr, path)
                path.pop()
        dfs(0, 0, [])
        return res