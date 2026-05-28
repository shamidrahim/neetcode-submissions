class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter('balloon')
        res = len(text)
        for c in balloon:
            res = min(countText[c] // balloon[c], res)

        return res
        