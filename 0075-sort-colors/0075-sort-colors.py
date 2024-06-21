class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        mid = 0
        while mid <= r:
            if nums[mid] == 0:
                nums[mid], nums[l] = nums[l], nums[mid]
                l += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
        return nums