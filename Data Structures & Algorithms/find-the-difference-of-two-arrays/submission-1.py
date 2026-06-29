class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1, res2 = [],[]
        nums1Set, nums2Set = set(nums1), set(nums2)
        for n in nums1Set:
            if n not in nums2Set:
                res1.append(n)
        for n in nums2Set:
            if n not in nums1Set:
                res2.append(n)
        return [res1, res2]