class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        maxOdd = 0
        minEven = len(s)
        for f in freq.values():
            if f % 2 != 0:
                maxOdd = max(maxOdd, f)
            elif f % 2 == 0:
                minEven = min(minEven, f)
        return maxOdd - minEven

        