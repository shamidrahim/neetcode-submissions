class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_set:
                return [nums_set[diff],i]
            nums_set[n] = i