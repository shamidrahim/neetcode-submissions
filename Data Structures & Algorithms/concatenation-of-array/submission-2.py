class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.capacity = len(nums)*2
        self.ans = self.capacity * [0]
        for i in range(len(nums)):
            self.ans[i] = nums[i]
            self.ans[i+len(nums)]=nums[i]
        return self.ans

        