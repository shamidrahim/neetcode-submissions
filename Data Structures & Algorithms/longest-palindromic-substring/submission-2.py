class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res_str = ''
        for i in range(len(s)):
            pal_len, maxStr = self.palindromeHelper(s, i, i)
            if pal_len > length:
                length = pal_len
                res_str = maxStr
            
            pal_len1, maxStr1 = self.palindromeHelper(s, i, i + 1)
            if pal_len1 > length:
                length = pal_len1
                res_str = maxStr1
        return res_str
    def palindromeHelper(self, s, l, r):
        maxLength = 0
        maxStr =''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > maxLength:
                maxLength = r - l + 1
                maxStr = s[l:r + 1]
            l -= 1
            r += 1
        return maxLength, maxStr




        