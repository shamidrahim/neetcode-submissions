class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs
    
    def helper(self, i: int, curComb: List, comb:List, n: int, k: int) -> None:
        if len(curComb) == k:
            comb.append(curComb.copy())
            return
        if i > n:
            return

        for j in range(i, n + 1):
            curComb.append(j)
            self.helper(j + 1, curComb, comb, n, k)
            curComb.pop()
            
        