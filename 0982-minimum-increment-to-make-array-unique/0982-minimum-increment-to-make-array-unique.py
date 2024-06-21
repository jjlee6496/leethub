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
                temp = nums[i-1]-nums[i]+1
                nums[i] += temp
                res += temp
        return res