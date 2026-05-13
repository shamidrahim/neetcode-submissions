class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]
        for i in range(N):
            dp[i][0] = 0
        for j in range(M + 1):
            if j >= weight[0]:
                dp[0][j] = (j // weight[0]) * profit[0]
        for r in range(1, N):
            for c in range(1, M + 1):
                skip = dp[r - 1][c]
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + dp[r][c - weight[r]]
                dp[r][c] = max(include, skip)
        return dp[N - 1][M]

