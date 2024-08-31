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
        graph = {i: [] for i in range(n)}
        # undirected graph
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        pq = [(-1.0, start_node)]
        probs = {start_node:1.0}

        while pq:
            curr_prob, curr_node = heapq.heappop(pq)
            curr_prob = -curr_prob

            if curr_node == end_node:
                return curr_prob
            if curr_prob < probs.get(curr_node, 0):
                continue
            for n_node, n_prob in graph[curr_node]:
                new_prob = curr_prob * n_prob
                if new_prob > probs.get(n_node, 0):
                    probs[n_node] = new_prob
                    heapq.heappush(pq, (-new_prob, n_node))
        return 0.0
