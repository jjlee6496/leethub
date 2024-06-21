class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                res += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return res