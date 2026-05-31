class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for w in words:
            consistent = True
            for c in w:
                if c not in allowed:
                    consistent = False
                    break
            
            if consistent:
                res += 1
        return res


        