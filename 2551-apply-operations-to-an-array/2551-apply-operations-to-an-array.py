class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] == nums[i] and nums[i] != 0:
                nums[i - 1] *= 2
                nums[i] = 0
        ans = [num for num in nums if num > 0]
        return ans + [0] * (len(nums) - len(ans))