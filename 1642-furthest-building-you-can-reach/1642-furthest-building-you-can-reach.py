class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        pq = []
        n = len(heights)
        for i in range(n - 1):
            gap = heights[i + 1] - heights[i]

            if gap > 0:
                heapq.heappush(pq, gap)

                if len(pq) > ladders:
                    bricks -= heapq.heappop(pq)
                if bricks < 0:
                    return i
        return n - 1