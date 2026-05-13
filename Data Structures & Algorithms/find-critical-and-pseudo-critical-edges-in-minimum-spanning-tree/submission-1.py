class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else:
            self.par[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e: e[2])
        mst_weight = 0
        uf = UnionFind(n)
        for n1, n2, w, i in edges:
            if uf.union(n1, n2):
                mst_weight += w

        critical, pseudo = [], []
        for v1, v2, c_weight, j in edges:
            weight = 0
            uf1 = UnionFind(n)
            for h1, h2, c1_weight, k in edges:
                if j != k and uf1.union(h1, h2):
                    weight += c1_weight
            if max(uf1.rank) != n or weight > mst_weight:
                critical.append(j)
                continue
                
            uf2 = UnionFind(n)
            uf2.union(v1, v2)
            weight = c_weight
            for p1, p2, p_weight, l in edges:
                if uf2.union(p1, p2):
                    weight += p_weight
            if weight == mst_weight:
                pseudo.append(j)

        return [critical, pseudo] 



        