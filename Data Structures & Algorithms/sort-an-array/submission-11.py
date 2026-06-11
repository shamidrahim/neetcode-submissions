class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countSort(arr, n, d):
            count = [0] * 10
            for num in arr:
                count[(num // d) % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]

            res = [0] * n
            for i in range(n - 1, -1, -1):
                idx = (arr[i] // d) % 10
                res[count[idx] - 1] = arr[i]
                count[idx] -= 1
            for i in range(n):
                arr[i] = res[i]

        def radixSort(arr):
            n = len(arr)
            max_elem = max(arr)
            d = 1
            while max_elem // d > 0:
                countSort(arr, n, d) 
                d *= 10

        neg = [-num for num in nums if num < 0]
        pos = [num for num in nums if num >=0]
        if neg:
            radixSort(neg)
            neg = [-num for num in reversed(neg)]
        if pos:
            radixSort(pos)

        return neg + pos
            