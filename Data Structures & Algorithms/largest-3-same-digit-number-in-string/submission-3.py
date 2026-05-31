class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = []
        i = 0
        for j in range(2, len(num)):
            if num[i] == num[i + 1] == num[i + 2]:
                res.append(num[i:j + 1])
            i += 1
        return max(res) if res else ""

        