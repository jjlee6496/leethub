class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target <= nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return mid if nums[mid] > target else mid + 1