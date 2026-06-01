class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        res = 0
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2

        return res + (res < len(s))        
        

        