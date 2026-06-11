class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def shellSort(nums, n):
            gap = n // 2
            while gap >= 1:
                for i in range(gap, n):
                    tmp = nums[i]
                    j = i - gap
                    while j >= 0 and nums[j] > tmp:
                        nums[j + gap] = nums[j]
                        j -= gap
                    nums[j + gap] = tmp
                gap //= 2
        n = len(nums)
        if n == 1:
            return nums
        shellSort(nums, n)
        return nums
            