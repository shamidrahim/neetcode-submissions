class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char = set()
        for c in s:
            if c in char:
                char.remove(c)
            else:
                char.add(c)
        return len(char) <= 1