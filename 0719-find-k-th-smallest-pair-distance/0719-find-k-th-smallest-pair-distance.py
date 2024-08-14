class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        def helper(dist):
            l = 0
            res = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res
        
        l, r = 0, max(nums)
        while l < r:
            m = l + ((r - l) // 2)
            pairs = helper(m)
            if pairs >= k:
                r = m
            else:
                l = m + 1
        return r