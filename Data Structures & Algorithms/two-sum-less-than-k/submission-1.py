class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        n = len(nums)
        nums.sort()
        for i, first_num in enumerate(nums):
            target = k - first_num
            left = i + 1
            right = n - 1
            first_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    first_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if first_index == -1:
                j = n - 1
            else:
                j = first_index - 1
            if i < j:
                max_sum = max(max_sum, first_num + nums[j])
        return max_sum

        