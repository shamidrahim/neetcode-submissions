class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def memo(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = memo(i + 1) + memo(i + 2)
            return cache[i]
        return memo(0)
        
        
        