class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] < stones[-2]:
                stones[-2] = stones[-2] - stones[-1]
                stones.remove(stones[-1])
            elif stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] > stones[-2]:
                stones[-1] = stones[-1] - stones[-2]
                stones.remove(stones[-2])
        return stones[0] if len(stones) else 0
