class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}
        for c in chars:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        res = 0
        for w in words:
            curWord = {}
            good = True
            for c in w:
                if c not in curWord:
                    curWord[c] = 0
                curWord[c] += 1
                if c not in count or curWord[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(w)
        return res



        