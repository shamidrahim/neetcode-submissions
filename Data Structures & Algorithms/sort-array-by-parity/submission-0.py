class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        o = 0
        for e in range(len(nums)):
            if nums[e] % 2 == 0:
                nums[o], nums[e] = nums[e], nums[o]
                o += 1
        return nums
        

        