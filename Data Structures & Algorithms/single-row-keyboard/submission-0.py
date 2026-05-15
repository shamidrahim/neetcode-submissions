class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        count = {}
        for i in range(len(keyboard)):
            count[keyboard[i]] = i
        j = 0
        res = 0
        for char in word:
            res += abs(j - count[char])
            j = count[char]
        return res


        