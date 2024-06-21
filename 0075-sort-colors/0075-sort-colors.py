class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        for i in range(len(nums)):
            while i >=l and i<= r and (nums[i]== 0 or nums[i]==2):
                if nums[i] == 0:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                elif nums[i] == 2:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
        return nums