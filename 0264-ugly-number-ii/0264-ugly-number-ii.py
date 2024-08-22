class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        minHeap = [1]
        visited = set()
        factors = [2, 3, 5]
        for i in range(n):
            num = heapq.heappop(minHeap)
            
            if i == n - 1:
                return num

            for f in factors:
                if num * f not in visited:
                    visited.add(num * f)
                    heapq.heappush(minHeap, num * f)

