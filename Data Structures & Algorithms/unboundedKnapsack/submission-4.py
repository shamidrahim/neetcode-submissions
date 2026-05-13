class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)
        for r in range(N):
            curRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + curRow[c - weight[r]]
                curRow[c] = max(include, skip)
            dp = curRow
        return dp[M]

