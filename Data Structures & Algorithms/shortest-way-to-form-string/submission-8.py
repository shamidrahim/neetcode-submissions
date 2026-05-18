class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t = 0
        res = 0
        for char in target:
            if char not in source:
                return -1
        while t < len(target):
            for s in range(len(source)):
                if t < len(target) and source[s] == target[t]:
                    t += 1
            res += 1
        return res


        
        