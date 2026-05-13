class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_cnt = 0
        for num in nums:
            if num == 1:
                count += 1
            if num == 0:
                count = 0
            max_cnt = max(count, max_cnt)
        return max_cnt

        