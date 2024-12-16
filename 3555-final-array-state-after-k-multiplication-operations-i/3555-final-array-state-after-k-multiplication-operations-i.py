class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        nums = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(nums)
        while k:
            n, i = heapq.heappop(nums)
            heapq.heappush(nums, (multiplier*n, i))
            k -= 1
        return [n[0] for n in sorted(nums, key=lambda x: x[1])]