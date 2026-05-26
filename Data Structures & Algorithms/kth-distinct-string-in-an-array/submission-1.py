class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        res = []
        for c in arr:
            hashmap[c] = 1 + hashmap.get(c, 0)
        for c in arr:
            if hashmap[c] == 1:
                k -= 1
                if k == 0:
                    return c
        return ""

        