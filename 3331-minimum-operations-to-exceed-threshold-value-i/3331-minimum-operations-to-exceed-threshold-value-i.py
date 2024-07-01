class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] >= k:
                r = mid
            elif nums[mid] < k:
                l = mid + 1
        return r
            