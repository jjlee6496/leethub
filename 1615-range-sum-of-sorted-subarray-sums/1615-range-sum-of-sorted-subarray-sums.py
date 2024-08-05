class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        res = []
        l = 0
        while l < n:
            for r in range(l, n):
                res.append(int(sum(nums[l:r+1])% (10**9 + 7)))
            l += 1
        return int(sum(sorted(res)[left-1:right]) % (10**9 + 7))



