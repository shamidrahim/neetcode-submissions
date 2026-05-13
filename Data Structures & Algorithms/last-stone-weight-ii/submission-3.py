class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum) // 2
        dp = defaultdict(int)
        n = len(stones)

        for i in range(n + 1):
            for t in range(target + 1):
                if t >= stones[i - 1]:
                    dp[(i, t)] = max(dp[(i - 1, t)], dp[(i - 1,t - stones[i - 1])] + stones[i - 1])
                else:
                    dp[(i, t)] = dp[(i - 1, t)]

        return stoneSum - 2 * dp[(n, target)]