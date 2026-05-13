class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float('inf')
        sum = 0
        for R in range(len(nums)):
            sum += nums[R]
            while sum >= target:
                length = min(R - L + 1, length)
                sum -= nums[L]
                L += 1
        return 0 if length == float('inf') else length
        