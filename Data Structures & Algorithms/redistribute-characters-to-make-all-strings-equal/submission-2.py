class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}
        for w in words:
            for c in w:
                if c not in count:
                    count[c] = 0
                count[c] += 1
        for values in count.values():
            if values % len(words):
                return False
        return True

        