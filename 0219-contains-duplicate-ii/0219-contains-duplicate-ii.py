class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        idx_map = {}
        for idx, num in enumerate(nums):
            if num in idx_map and idx - idx_map[num] <= k:
                return True
            idx_map[num] = idx
        return False
