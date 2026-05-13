class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp7, dp30 = deque(), deque()
        dp = 0
        for d in days:
            while dp7 and dp7[0][0] + 7 <= d:
                dp7.popleft()
            while dp30 and dp30[0][0] + 30 <= d:
                dp30.popleft()
            dp7.append([d, costs[1] + dp])
            dp30.append([d, costs[2] + dp])
            dp = min(costs[0] + dp, dp7[0][1], dp30[0][1])
        return dp