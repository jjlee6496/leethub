class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mask = 1 << len(nums)
        res = [[] for _ in range(mask)]
        for m in range(mask):
            for i, x in enumerate(nums):
                if m & 1 << i:
                    res[m].append(x)
        return res
