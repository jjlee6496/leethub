class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        prev = 0
        curr = 0
        for num in nums:
            if num > prev:
                curr += num
            else:
                curr = num
            prev = num
            res = max(res, curr)
        return res