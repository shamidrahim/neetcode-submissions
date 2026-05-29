class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase, decrease = True, True
        for i in range(len(nums) - 1):
            if not (nums[i + 1] >= nums[i]):
                increase = False
            if not (nums[i + 1] <= nums[i]):
                decrease = False
        return increase or decrease


        