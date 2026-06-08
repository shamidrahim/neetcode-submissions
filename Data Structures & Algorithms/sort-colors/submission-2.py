class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxNum = max(nums)
        count = [0] * (maxNum + 1)
        for n in nums:
            count[n] += 1
        i = 0
        for n in range(maxNum + 1):
            for j in range(count[n]):
                nums[i] = n
                i += 1
        