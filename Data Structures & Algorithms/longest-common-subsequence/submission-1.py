class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        for i in range((len(text1))):
            curRow = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    curRow[j + 1] = 1 + dp[j]
                else:
                    curRow[j + 1] = max(dp[j + 1], curRow[j])
            dp = curRow
        return dp[len(text2)]  