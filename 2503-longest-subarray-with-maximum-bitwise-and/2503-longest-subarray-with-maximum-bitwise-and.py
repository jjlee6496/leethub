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
                res = max(res, curr)
            else:
                curr = 0
        return res