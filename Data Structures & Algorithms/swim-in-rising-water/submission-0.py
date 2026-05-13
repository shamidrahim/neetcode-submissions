class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap =[[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                neir, neic = r + dr, c + dc
                if (neir < 0 or neic < 0 or neir >= n or neic >= n
                or (neir, neic) in visit):
                    continue
                visit.add((neir, neic))
                heapq.heappush(minHeap, [max(t, grid[neir][neic]), neir, neic])




        