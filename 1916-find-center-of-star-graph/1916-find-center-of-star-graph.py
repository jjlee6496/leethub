class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        cnt = Counter()
        for u, v in edges:
            cnt[u] += 1
            cnt[v] += 1
        
        for k, v in cnt.items():
            if v == len(edges):
                return k