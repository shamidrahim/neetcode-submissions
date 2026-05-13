class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            for a in range(amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
    
        