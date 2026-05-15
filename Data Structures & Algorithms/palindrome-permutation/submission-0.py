class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        for c in s:
            count[c] =  1 + count.get(c, 0)
        odds = sum(val % 2 for val in count.values())
        return odds <= 1