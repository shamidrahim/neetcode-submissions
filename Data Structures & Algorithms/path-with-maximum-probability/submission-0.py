class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        visit = set()
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))

        maxHeap = [(-1, start_node)]
        while maxHeap:
            prob, cur = heapq.heappop(maxHeap)
            visit.add(cur)
            if cur == end_node:
                return -prob
            for neicur, neiprob in adj[cur]:
                if neicur not in visit:
                    heapq.heappush(maxHeap, (neiprob * prob, neicur))
        return 0.0

