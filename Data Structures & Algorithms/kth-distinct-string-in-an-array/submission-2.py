class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct, seen = set(), set()
        for c in arr:
            if c in distinct:
                distinct.remove(c)
                seen.add(c)
            elif c not in seen:
                distinct.add(c)
        for c in arr:
            if c in distinct:
                k -= 1
                if k == 0:
                    return c
        return ""

        