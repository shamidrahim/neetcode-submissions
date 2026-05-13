class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = -1
        for i in range(n - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr

        