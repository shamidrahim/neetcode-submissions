class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        gridSum = 0
        gridSqSum = 0
        for i in range(n):
            for j in range(n):
                gridSum += grid[i][j]
                gridSqSum += grid[i][j] * grid[i][j]
        
        totSum = (n * n * (n * n + 1))//2
        diff = gridSum - totSum
        totSqSum = (n * n * (n * n + 1) * (2 * n * n + 1)) // 6
        sqDiff = gridSqSum - totSqSum
        sum = sqDiff // diff
        a = (sum + diff) // 2
        b = sum - a
        return [a, b]
        