class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = []
        for i in range(n):
            for j in range(n):
                value = abs(grid[i][j])
                r = (value - 1) // n
                c = (value - 1) % n

                if grid[r][c] < 0:
                    repeated = value
                else:
                    grid[r][c] *= -1
        res.append(repeated)
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    res.append(i * n + j + 1)
        return res

        