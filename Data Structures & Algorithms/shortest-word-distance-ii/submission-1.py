class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dictInd = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.dictInd[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        ind1 = self.dictInd[word1]
        ind2 = self.dictInd[word2]
        res = float("inf")
        l1, l2 = 0, 0
        while l1 < len(ind1) and l2 < len(ind2):
            res = min(res, abs(ind1[l1] - ind2[l2]))
            if ind1[l1] < ind2[l2]:
                l1 += 1
            else:
                l2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
