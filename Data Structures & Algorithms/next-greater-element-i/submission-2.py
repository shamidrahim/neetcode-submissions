class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    while j + 1 < len(nums2) and nums2[j + 1] <= nums1[i]:
                        j += 1
                    if j + 1 >= len(nums2):
                        res.append(-1)
                    else:
                        res.append(nums2[j + 1])
                j += 1
                
        return res

        