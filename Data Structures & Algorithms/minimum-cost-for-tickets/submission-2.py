class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0]* (n + 1)
        for i in range(n - 1, -1 , -1):
            dp[i] = float('inf')
            j = i
            for c, d in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])
        return dp[0]

        