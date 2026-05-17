class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        row1, col1 = len(mat1), len(mat1[0])
        row2, col2 = len(mat2), len(mat2[0])
        res = []
        for m in range(row1):
            temp = []
            for n in range(col2):
                sum = 0
                for k in range(col1):
                    sum += mat1[m][k] * mat2[k][n]
                temp.append(sum)
            res.append(temp)
                
        return res

