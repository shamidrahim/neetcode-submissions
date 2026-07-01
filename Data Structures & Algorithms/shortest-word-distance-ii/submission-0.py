class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dictInd = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.dictInd[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        ind1 = self.dictInd[word1]
        ind2 = self.dictInd[word2]
        res = float("inf")
        for i1 in ind1:
            for i2 in ind2:
                res = min(res, abs(i1 - i2))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
