class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = len(wordsDict)
        w1, w2 = 0,0
        for i, w in enumerate(wordsDict):
            if w == word1:
                w1 = i
            if w == word2:
                w2 = i
            if w1 or w2:
                res = min(res, abs(w2 - w1))
        return res