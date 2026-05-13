class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        max_area = []
        def bfs(r, c):
            area = 1
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >=rows or nc 
                        >=cols or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area.append(bfs(r, c))
                    

        return max(max_area) if max_area else 0
        

        