class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        def dfs(i, total):
            if i == N:
                return total == target
            
            return (dfs(i + 1, total + nums[i]) + 
            dfs(i + 1, total - nums[i]))
        return dfs(0, 0)    