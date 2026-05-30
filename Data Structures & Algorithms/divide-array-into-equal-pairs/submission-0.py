class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for value in count.values():
            if value % 2 != 0:
                return False
        return True
        