class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i, n in enumerate(nums):
            nums_set[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_set and nums_set[diff] != i:
                return [i, nums_set[diff]]
        return []