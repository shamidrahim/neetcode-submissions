class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {}
        double = missing = 0
         
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] = 1 + count.get(grid[i][j], 0)
        for num in range(1, n * n + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                double = num
        return [double, missing]
        