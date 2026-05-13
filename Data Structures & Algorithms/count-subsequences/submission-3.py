class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        for k in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[k][j] = dp[k + 1][j]
                if s[k] == t[j]:
                    dp[k][j] += dp[k + 1][j + 1]
        return dp[0][0]
        