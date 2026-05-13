class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, p1):
        while p1 != self.par[p1]:
            p1 = self.find(self.par[p1])
        return self.par[p1]

    def union(self, v1, v2):
        r1, r2 = self.find(v1), self.find(v2)
        if r1 == r2:
            return False
        if self.rank[r1] > self.rank[r2]:
            self.par[r2] = r1
            self.rank[r1] += self.rank[r2]
        else:
            self.par[r1] = r2
            self.rank[r2] += self.rank[r1]
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        total_w, components = 0, n
        for u, v, w in edges:
            heapq.heappush(minHeap, [w, u, v])

        uf = UnionFind(n)
        while components > 1 and minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)
            if uf.union(n1, n2):
                total_w += weight
                components -= 1
        return total_w if components == 1 else -1

