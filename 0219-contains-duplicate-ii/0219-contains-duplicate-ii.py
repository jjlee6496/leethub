class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = 0
        s = set()
        for r in range(len(nums)):
            if r - l > k:
                s.remove(nums[l])
                l += 1
            if nums[r] in s:
                return True
            s.add(nums[r])
        return False
