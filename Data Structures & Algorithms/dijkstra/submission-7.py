class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        for s, d, w in edges:
            adjlist[s].append([d, w])
        res = {}
        heap = [[0, src]]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in res:
                continue
            res[n1] = w1
            for n2, w2 in adjlist[n1]:
                if n2 not in res:
                    heapq.heappush(heap, [w1 + w2, n2])
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res

