class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openCnt = closeCnt = 0
        for c in s:
            closeCnt += c == ')'

        res = []
        for c in s:
            if c == '(':
                if openCnt == closeCnt:
                    continue
                openCnt += 1
            elif c == ')':
                closeCnt -= 1
                if openCnt == 0:
                    continue
                openCnt -= 1
            res.append(c)
        return ''.join(res)