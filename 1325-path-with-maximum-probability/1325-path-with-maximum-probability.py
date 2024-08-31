class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        adj = {i:[] for i in range(n)}
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i])) # src: dst, weight
            adj[edges[i][1]].append((edges[i][0], succProb[i])) # dst: src, weight
        
        res = {i:0.0 for i in range(n)}
        res[start_node] = 1.0
        pq = [(-1.0 ,start_node)] # maxHeap
        while pq:
            w1, n1 = heapq.heappop(pq)
            w1 = -w1 # 원래대로

            if res[n1] < w1:
                res[n1] = w1

            for n2, w2 in adj[n1]:
                if w1 * w2 > res[n2]:
                    heapq.heappush(pq, (-(w1 * w2), n2))
        return res[end_node]