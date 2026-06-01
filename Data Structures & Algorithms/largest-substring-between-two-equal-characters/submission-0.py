class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == s[j]:
                    res = max(res, j - i - 1)
        return res
            


        