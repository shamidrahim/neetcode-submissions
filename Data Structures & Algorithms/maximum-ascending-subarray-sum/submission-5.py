class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        sumCount = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] >= nums[i]:
                sumCount = 0
            sumCount += nums[i]
            res = max(res, sumCount)
        return res

        