class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        return max([num for num, freq in count.items() if freq == 1], default = -1)

        