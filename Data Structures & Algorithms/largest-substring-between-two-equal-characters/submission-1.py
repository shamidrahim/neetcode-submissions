class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        firstIdx = {}
        lastIdx = {}
        for i, c in enumerate(s):
            if c not in firstIdx:
                firstIdx[c] = i
            else:
                lastIdx[c] = i
        for c in lastIdx:
            res = max(res, lastIdx[c] - firstIdx[c] - 1)
        
        return res
            


        