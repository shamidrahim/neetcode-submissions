class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        curSum = 0
        res = len(nums) + 1
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                res = min(R - L + 1, res)
                curSum -= nums[L]
                L += 1
        return 0 if res == len(nums) + 1 else res

