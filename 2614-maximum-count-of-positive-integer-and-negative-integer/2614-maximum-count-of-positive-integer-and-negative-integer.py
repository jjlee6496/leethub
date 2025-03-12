class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = bisect_left(nums, 0)
        r = bisect_right(nums, 0)
        if r == 0:
            return len(nums)
        return max(l, len(nums) - r)