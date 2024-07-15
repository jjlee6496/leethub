class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt = Counter(nums)
        perm = []
        res = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in cnt:
                if cnt[n] > 0:
                    perm.append(n)
                    cnt[n] -= 1

                    dfs()

                    cnt[n] += 1
                    perm.pop()
        dfs()
        return res