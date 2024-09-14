class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        curr = 0
        res = 0
        for num in nums:
            if num == max_num:
                curr += 1
            else:
                res = max(res, curr)
                curr = 0
        res = max(res, curr)
        return res