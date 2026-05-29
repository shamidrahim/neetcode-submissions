class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        res = -1
        for num in arr:
            freq[num] = 1 + freq.get(num, 0)
        
        for num in arr:
            if num == freq[num]:
                res = max(res, num)       
        return res

        