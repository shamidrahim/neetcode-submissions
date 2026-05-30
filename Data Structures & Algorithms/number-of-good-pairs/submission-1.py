class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        for c in count.values():
            res += (c * (c - 1)) // 2
        return res

        