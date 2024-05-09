class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        prices = [float("inf")]*n
        prices[src] = 0
        for i in range(k+1):
            temp = prices[:]
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            prices = temp
        return -1 if prices[dst] == float("inf") else prices[dst]