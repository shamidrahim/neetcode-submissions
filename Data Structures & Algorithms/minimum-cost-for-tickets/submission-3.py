class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.append(days[-1] + 30)
        n = len(days)
        dp = [0]* (n + 1)
        last7 = last30 = n
        for i in range(n - 2, -1 , -1):
            dp[i] = dp[i + 1] + costs[0]
            while last7 > i + 1 and days[last7 - 1] >= days[i] + 7:
                last7 -= 1
            dp[i] = min(dp[i], dp[last7] + costs[1])
            while last30 > i + 1 and days [last30 - 1] >= days[i] + 30:
                last30 -= 1
            dp[i] = min(dp[i], dp[last30] + costs[2])

        return dp[0]

        