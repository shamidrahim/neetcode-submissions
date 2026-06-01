class Solution:
    def maxScore(self, s: str) -> int:
        n, res = len(s), 0
        one, zero = 0, 0
        if s[0] == '0':
            zero += 1
        else:
            one += 1
        res = float('-inf')
        for i in range(1, len(s)):
            res = max(res, zero - one)
            if s[i] == '0':
                zero += 1
            else:
                one += 1
        return res + one
        