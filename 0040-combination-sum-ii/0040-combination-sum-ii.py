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
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]: # 중복 제거
                    continue
                if curr + candidates[i] > target: # 더 진행해봤자 의미 없으므로 종료
                    break
                dfs(i + 1, curr + candidates[i], path + [candidates[i]])
        dfs(0, 0, [])
        return res