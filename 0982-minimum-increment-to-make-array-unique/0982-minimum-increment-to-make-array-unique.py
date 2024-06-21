class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        res = 0
        for i in range(len(nums)+max(nums)):
            if cnt[i] > 1:
                extra = cnt[i] - 1
                cnt[i+1] += extra
                res += extra
        return res