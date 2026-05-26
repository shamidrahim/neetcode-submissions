class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = OrderedDict()
        res = []
        for c in arr:
            hashmap[c] = 1 + hashmap.get(c, 0)
        for keys, values in hashmap.items():
            if values == 1:
                res.append(keys)
        return "" if k - 1 >= len(res) else res[k - 1]

        