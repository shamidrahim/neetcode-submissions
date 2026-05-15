class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for num in arr:
            if num + 1 in arr:
                count += 1
        return count
        