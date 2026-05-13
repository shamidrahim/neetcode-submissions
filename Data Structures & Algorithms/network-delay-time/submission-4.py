class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        visit = set()
        minHeap = [[0, k]]
        t = 0
        while minHeap:
            ti, vi = heapq.heappop(minHeap)
            if vi in visit:
                continue
            visit.add(vi)
            t = max(t, ti)
            for vi2, ti2 in adj[vi]:
                if vi2 not in visit:
                    heapq.heappush(minHeap, [ti + ti2, vi2])
        return t if len(visit) == n else -1