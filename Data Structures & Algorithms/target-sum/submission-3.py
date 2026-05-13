class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(N):
            nextDp = defaultdict(int)
            for curSum, count in dp.items():
                nextDp[curSum + nums[i]] += count
                nextDp[curSum - nums[i]] += count
            dp = nextDp
        return dp[target]