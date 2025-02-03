class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc_win = 1
        dec_win = 1
        res = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                inc_win = 1
                dec_win += 1
            elif nums[i] > nums[i - 1]:
                inc_win += 1
                dec_win = 1
            else:
                inc_win, dec_win = 1, 1
            res = max(res, inc_win, dec_win)
        return max(res, inc_win, dec_win)