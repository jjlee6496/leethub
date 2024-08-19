class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def backtrack(i, curr, path):
            if i >= len(candidates):
                return
            
            if curr == target:
                res.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                if curr + candidates[j] > target:
                    break
                path.append(candidates[j])
                backtrack(j, curr + candidates[j], path)
                path.pop()
        backtrack(0, 0, [])
        return res