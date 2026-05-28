class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_set:
                return [nums_set[diff], i]
            nums_set[num] = i
        