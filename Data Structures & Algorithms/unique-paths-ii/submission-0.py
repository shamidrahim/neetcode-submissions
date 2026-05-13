class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        def memo(r, c, cache):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c]>0:
                return cache[r][c]
            if r ==rows-1 and c == cols -1:
                return 1
            cache[r][c] = memo(r+1,c,cache) + memo(r,c+1,cache)

            return cache[r][c]
        return memo(0,0,[[0]*cols for i in range(rows)])

            
        