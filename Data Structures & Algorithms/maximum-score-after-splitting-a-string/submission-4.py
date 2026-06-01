class Solution:
    def maxScore(self, s: str) -> int:
        n, res = len(s), 0
        one, zero = s.count('1'), 0
        for i in range(n - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)
        return res