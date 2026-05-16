class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = list(s)
        for lis in shift:
            if lis[0] == 0:
                for _ in range(lis[1]):
                    left = s.pop(0)
                    s.append(left)
            else:
                for _ in range(lis[1]):
                    right = s.pop()
                    s.insert(0, right)
        return ''.join(s)        