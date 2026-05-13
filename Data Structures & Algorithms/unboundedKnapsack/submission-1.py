class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfsHelper(0, profit, weight, capacity)
    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(weight):
            return 0
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)
        new_cap = capacity - weight[i]
        if new_cap >= 0:
            p = profit[i] + self.dfsHelper(i, profit, weight, new_cap)
            maxProfit = max(p, maxProfit)
        return maxProfit

