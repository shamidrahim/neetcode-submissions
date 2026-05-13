class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp7, dp30 = deque(), deque()
        dp = 0
        last7 = last30 = 0
        for i in range(len(days) - 1, -1, -1):
            dp += costs[0]
            while dp7 and dp7[-1][0] >=  days[i] + 7:
                last7 = dp7.pop()[1]
            dp = min(dp, costs[1] + last7)
            while dp30 and dp30[-1][0] >= days[i] + 30:
                last30 = dp30.pop()[1]
            dp = min(dp, costs[2] + last30)
            dp7.appendleft([days[i], dp])
            dp30.appendleft([days[i], dp])
        return dp