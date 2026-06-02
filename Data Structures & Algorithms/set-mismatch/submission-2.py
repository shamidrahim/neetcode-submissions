class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        res = [0, 0]
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for i in range(1, len(nums) + 1):
            if i not in count:
                res[1] = i
            if i in count and count[i] == 2:
                res[0] = i
        return res

         
        