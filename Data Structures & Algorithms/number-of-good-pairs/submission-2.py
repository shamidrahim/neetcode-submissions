class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                res += count[n]
                count[n] += 1
        return res

        