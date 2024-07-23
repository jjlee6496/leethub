class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = Counter(nums)
        max_heap = []
        for k, v in cnt.items():
            heapq.heappush(max_heap, (-v, k))
        res = []
        while max_heap:
            freq, num = heapq.heappop(max_heap)
            res.extend([num]*-freq)
        return reversed(res)
        