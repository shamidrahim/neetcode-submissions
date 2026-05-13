class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        res = 0

        for i in range(len(t)):
            l, r = i, i
            while l >= 0 and r < len(t) and t[l] == t[r]:
                if t[l] != '#':
                    res += 1
                l -= 1
                r += 1

        return res
            