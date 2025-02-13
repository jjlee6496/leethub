class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            x = heapq.heappop(nums)
            if x >= k:
                return res
            y = heapq.heappop(nums)
            heapq.heappush(nums, 2 * x + y)

            res += 1
        return res