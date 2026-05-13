class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                nums[l] = nums[r]
            if nums[l] != nums[l - 1]:
                l += 1
        return l


        
                


        