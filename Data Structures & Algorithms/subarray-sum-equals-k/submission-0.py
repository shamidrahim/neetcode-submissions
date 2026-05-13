class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        res = curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            res += count.get(diff, 0)
            count[curSum] = 1 + count.get(curSum, 0)
        return res
        


        