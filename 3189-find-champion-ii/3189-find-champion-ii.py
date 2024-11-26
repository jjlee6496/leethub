class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [0] * n
        for _, v in edges:
            graph[v] = 1
        
        if n - sum(graph) > 1:
            return -1
        
        for i in range(n):
            if graph[i] == 0:
                return i
        return -1