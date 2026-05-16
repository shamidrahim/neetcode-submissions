class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        @staticmethod
        def check(x, y):
            n, m = len(picture), len(picture[0])
            cnt = 0
            for i in range(n):
                cnt += 1 if picture[i][y] == 'B' else 0
            for j in range(m):
                if j != y:
                    cnt += 1 if picture[x][j] == 'B' else 0
            return picture[x][y] == 'B' and cnt == 1

        n, m = len(picture), len(picture[0])
        answer = 0
        for j in range(m):
            answer += 1 if check(0,j) else 0
        for i in range(1, n):
            answer += 1 if check(i,0) else 0
        for j in range(m):
            picture[0][j] = '1' if picture[0][j] == 'B' else '0'
        for i in range(n):
            picture[i][0] = '1' if picture[i][0] == 'B' else '0'

        for i in range(1, n):
            for j in range(1, m):
                if picture[i][j] == 'B':
                    picture[i][0] = chr(ord(picture[i][0]) + 1)
                    picture[0][j] = chr(ord(picture[0][j]) + 1)
        
        for i in range(1, n):
            for j in range(1, m):
                if picture[i][j] == 'B':
                    if picture[0][j] == '1' and picture[i][0] == '1':
                        answer += 1

        return answer






        