class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        count = 0
        r_count = [0] * n
        c_count = [0] * m
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    r_count[i] += 1
                    c_count[j] += 1
        answer = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B' and r_count[i] == 1 and c_count[j] == 1:
                    answer += 1
        return answer




        