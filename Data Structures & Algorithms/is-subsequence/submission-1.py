class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if m == 0:
            return n == 0
        store = [[m + 1] * 26 for _ in range(m)]
        store[m - 1][ord(t[m - 1]) - ord('a')] = m - 1
        for i in range(m - 2, -1, -1):
            store[i] = store[i + 1][:]
            store[i][ord(t[i])- ord('a')] = i
        i, j = 0, 0
        while i < n and j < m:
            j = store[j][ord(s[i]) - ord('a')] + 1
            if j > m:
                return False
            i += 1
        return i == n
        