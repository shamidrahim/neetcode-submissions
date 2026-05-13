class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            nextPerm = []
            for p in res:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, n)
                    nextPerm.append(pCopy)
            res = nextPerm
        return res

        