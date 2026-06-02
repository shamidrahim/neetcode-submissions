class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        charIdx = {}
        for i, c in enumerate(s):
            if c in charIdx:
                res = max(res, i - charIdx[c] - 1)
            else:
                charIdx[c] = i
        
        return res
            


        