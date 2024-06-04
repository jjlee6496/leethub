class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = set(nums)
        res = -1
        for num in nums:
            if -num in cnt:
                res = max(res, abs(num))
        return res