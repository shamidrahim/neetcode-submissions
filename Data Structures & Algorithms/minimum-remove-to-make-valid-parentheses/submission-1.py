class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        count = 0
        for i, c in enumerate(s):
            if c == '(':
                count += 1
            elif c == ')' and count > 0:
                count -= 1
            elif c == ')':
                arr[i] = ''
        
        res = []
        for c in reversed(arr):
            if c == '(' and count > 0:
                count -= 1
            else:
                res.append(c)
        return ''.join(reversed(res))