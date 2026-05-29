class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        countInc = 1
        countDec = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                countInc += 1
            elif nums[i] < nums[i - 1]:
                countDec += 1
            else:
                countDec += 1
                countInc += 1
            
        if countInc == n or countDec == n:
            return True
        return False


        