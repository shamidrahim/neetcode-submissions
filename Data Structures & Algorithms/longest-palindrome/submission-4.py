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

        for value in count.values():
            if value % 2:
                res += 1
                break
        return res        
        

        