from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = self._merge_sort(nums, 0, len(nums) - 1)
        largest_num = ''.join(map(str, sorted_nums))
        return "0" if largest_num[0] == "0" else largest_num

    def _merge_sort(self, nums: List[int],left: int, right: int):
        if left >= right:
            return [nums[left]]
        mid = (left + right) // 2 
        left_half = self._merge_sort(nums, left, mid)
        right_half = self._merge_sort(nums, mid + 1, right)
        return self._merge(left_half, right_half)



    def _merge(self, left_half: List[int], right_half: List[int]) -> List[int]:
        sorted_nums = []
        l, r = 0, 0
        while l < len(left_half) and r < len(right_half):
            if self._compare(left_half[l], right_half[r]):
                sorted_nums.append(left_half[l])
                l += 1
            else:
                sorted_nums.append(right_half[r])
                r += 1
        sorted_nums.extend(left_half[l:])
        sorted_nums.extend(right_half[r:])
        return sorted_nums
    def _compare(self, first_num: int, second_num: int) -> bool:
        return str(first_num) + str(second_num) > str(second_num) + str(first_num)


        
        