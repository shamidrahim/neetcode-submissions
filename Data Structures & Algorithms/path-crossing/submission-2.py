class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        x, y = 0, 0
        visit.add(self.hash(x, y))
        for p in path:
            if p == 'N':
                y += 1
            elif p == "S":
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            pos = self.hash(x, y)
            if pos in visit:
                return True
            visit.add(pos)
        
        return False
    def hash(self, x: int, y: int) -> int:
        return(x << 32) + y
        