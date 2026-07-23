class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        l1 = l2 = 0
        while l1 < len(encoded1) and l2 < len(encoded2):
            val1, freq1 = encoded1[l1]
            val2, freq2 = encoded2[l2]
            product_val = val1 * val2
            product_freq = min(freq1, freq2)
            encoded1[l1][1] -= product_freq
            encoded2[l2][1] -= product_freq
            if encoded1[l1][1] == 0:
                l1 += 1
            if encoded2[l2][1] == 0:
                l2 += 1
            if not res or res[-1][0] != product_val:
                res.append([product_val, product_freq])
            else:
                res[-1][1] += product_freq
        return res

        