class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common_dict = {}
        m, n  = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                common_dict[mat[i][j]] = 1 + common_dict.get(mat[i][j], 0)
        res = float('inf')
        for keys, values in common_dict.items():
            if values == m:
                res = min(res, keys)
        
        return -1 if res == float('inf') else res

        