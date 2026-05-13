class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for src, dst, w in edges:
            adj[src].append([dst, w])
            adj[dst].append([src, w])

        minHeap = []
        for nei, w in adj[0]:
            heapq.heappush(minHeap, [w, 0, nei])
        mst = []
        visit = set()
        visit.add(0)
        total = 0
        while len(visit) < n and minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            total += w    
            visit.add(n2)
            mst.append([n1, n2])
            for nei, weight in adj[n2]:
                if nei not in visit:
                    heapq.heappush(minHeap, [weight, n2, nei])
        return total if len(visit) == n else -1




        