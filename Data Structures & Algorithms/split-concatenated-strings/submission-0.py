class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        res = ""
        for i in range(len(strs)):
            rev = strs[i][::-1]
            other = "".join(strs[i + 1:]) + "".join(strs[:i])

            for s in (strs[i], rev):
                for j in range(len(s)):
                    candidate = s[j:] + other + s[:j]
                    if candidate > res:
                        res = candidate
        return res            
        