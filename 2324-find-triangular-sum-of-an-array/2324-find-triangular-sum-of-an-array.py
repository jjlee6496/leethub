class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        for _ in range(N-1):
            for i in range(1, len(nums)):
                nums[i-1] = (nums[i-1] + nums[i]) % 10
            nums[:] = nums[:-1]
        return nums[0]
