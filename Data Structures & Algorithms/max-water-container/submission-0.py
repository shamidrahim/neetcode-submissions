class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxh = 0
        while l < r:
            if heights[l] < heights[r]:
                water = heights[l] * (r - l)
                maxh = max(maxh, water)
                l += 1
            else:
                water = heights[r] * (r - l)
                maxh = max(maxh, water)
                r -= 1
        return maxh

        