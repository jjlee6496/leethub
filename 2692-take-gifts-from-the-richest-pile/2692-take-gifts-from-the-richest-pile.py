class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        while k:
            num = heapq.heappop(gifts)
            heapq.heappush(gifts, -1 * int(math.sqrt(-num)))
            k -= 1
        return -sum(gifts)

