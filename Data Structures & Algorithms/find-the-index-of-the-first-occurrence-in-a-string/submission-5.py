class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        base1, mod1 = 31, 10**9 + 7
        base2, mod2 = 37, 10**9 + 9
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        power1, power2 = (base1**m) % mod1, (base2**m) % mod2
        needle_hash1 , needle_hash2 = 0, 0
        haystack_hash1, haystack_hash2 = 0, 0

        for i in range(m):
            needle_hash1 = (needle_hash1 * base1 + ord(needle[i])) % mod1
            needle_hash2 = (needle_hash2 * base2 + ord(needle[i])) % mod2
            haystack_hash1 = (haystack_hash1 * base1 + ord(haystack[i])) % mod1
            haystack_hash2 = (haystack_hash2 * base2 + ord(haystack[i])) % mod2
            

        for i in range(n - m + 1):
            if haystack_hash1 == needle_hash1 and haystack_hash2 == needle_hash2:
                return i
            if i + m < n:
                haystack_hash1 = (haystack_hash1 * base1 - ord(haystack[i]) 
                * power1 + ord(haystack[i + m])) % mod1
                haystack_hash2 = (haystack_hash2 * base2 - ord(haystack[i]) 
                * power2 + ord(haystack[i + m])) % mod2
                haystack_hash1 = (haystack_hash1 + mod1) % mod1
                haystack_hash2 = (haystack_hash2 + mod2) % mod2
        return -1



        