class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.rank[root_x] += 1
                self.parent[root_y] = root_x
            return True
        return False

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, e in enumerate(edges):
            e.append(i) # (u, v, w, i)
        edges.sort(key = lambda x: x[2]) # sort by weight

        def make_mst(include=None, exclude=None):
            uf = UnionFind(n)
            weight = 0
            used = 0
            if include is not None:
                n1, n2, w, i = edges[include]
                uf.union(n1, n2)
                weight += w
                used += 1
            for i, (n1, n2, w, _) in enumerate(edges):
                if i == exclude:
                    continue
                if uf.union(n1, n2):
                    weight += w
                    used += 1
                if used == n - 1:
                    break
            return weight if used == n - 1 else float('inf')
        
        mst_weight = make_mst()
        critical, pseudo = [], []
        for i in range(len(edges)):
            w1, w2 = make_mst(exclude=i), make_mst(include=i)
            if w1 > mst_weight:
                critical.append(edges[i][3])
            elif w2 == mst_weight:
                pseudo.append(edges[i][3])
        return [critical, pseudo]
