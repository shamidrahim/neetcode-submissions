class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        min_cost = 0
        visit = set()
        visit.add(0)
        minHeap = []
        for c, idx in adj[0]:
            heapq.heappush(minHeap, [c, idx])

        while minHeap and len(visit) < len(points):
            cost1, index = heapq.heappop(minHeap)
            if index in visit:
                continue
            visit.add(index)
            min_cost += cost1
            for neicost, neiIdx in adj[index]:
                if neiIdx not in visit:
                    heapq.heappush(minHeap, [neicost, neiIdx])

        return min_cost


        