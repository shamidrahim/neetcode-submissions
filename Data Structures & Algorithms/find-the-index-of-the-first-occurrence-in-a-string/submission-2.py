class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        s = needle + "$" + haystack 
        n = len(s)
        l = r = 0
        z = [0] * n
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        for i in range(len(needle) + 1,n):
            if z[i] == len(needle):
                return i - len(needle) - 1
        return -1               
        
                



        