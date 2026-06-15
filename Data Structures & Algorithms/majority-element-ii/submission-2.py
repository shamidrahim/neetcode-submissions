class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums1 = nums2 = -1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == nums1:
                cnt1 += 1
            elif num == nums2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                nums1 = num
            elif cnt2 == 0:
                cnt2 = 1
                nums2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == nums1:
                cnt1 += 1
            elif num == nums2:
                cnt2 += 1


        res = []
        if cnt1 > n // 3:
            res.append(nums1)
        if cnt2 > n // 3:
            res.append(nums2)
        return res



