class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        for num in nums1:
            seen[num] = 1
        res = []
        for num in nums2:
            if num in seen and seen[num] == 1:
                seen[num] = 0
                res.append(num)
        return res