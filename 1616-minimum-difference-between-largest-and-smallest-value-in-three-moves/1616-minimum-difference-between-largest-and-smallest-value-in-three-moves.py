class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 5:
            return 0

        # nums.sort()
        res = float('inf')

        # for l in range(4):
        #     r = len(nums) - 4 + l # 3,2,1,0
        #     res = min(res, nums[r] - nums[l])
        # return res
        maxs = sorted(heapq.nlargest(4, nums))
        mins = sorted(heapq.nsmallest(4, nums))
        for i in range(4):
            res = min(res, maxs[i] - mins[i])
        return res