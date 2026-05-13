class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, node):
        cur = node
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            self.par[pu] = pv
            self.rank[pv] += self.rank[pu]
        else:
            self.par[pv] = self.par[pu]
            self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res