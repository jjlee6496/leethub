class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.size[root_x] += self.size[root_y]
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
            e.append(i)  # [u, v, w, i]

        edges.sort(key=lambda x: x[2])  # sort by weight

        def make_mst(to_include=-1, to_exclude=-1):
            uf = UnionFind(n)
            weight = 0
            if to_include != -1:
                n1, n2, w, _ = edges[to_include]
                uf.union(n1, n2)
                weight += w
            for i, (n1, n2, w, _) in enumerate(edges):
                if i == to_exclude:
                    continue
                if uf.union(n1, n2):
                    weight += w
            # Check if all nodes are connected by counting unique roots
            root_set = set(uf.find(x) for x in range(n))
            return weight if len(root_set) == 1 else float('inf')

        critical, pseudo = [], []
        mst_weight = make_mst()

        for i in range(len(edges)):
            # Check if the edge is critical
            if make_mst(to_exclude=i) > mst_weight:
                critical.append(edges[i][3])
            # Check if the edge is pseudo-critical
            elif make_mst(to_include=i) == mst_weight:
                pseudo.append(edges[i][3])

        return [critical, pseudo]
