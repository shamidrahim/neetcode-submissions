class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        maxh = 0
        while l < r:
            if heights[l] > heights[r]:
                maxh = max(heights[r] * (r - l), maxh)
                r -= 1
            else:
                maxh = max(heights[l] * (r - l), maxh)
                l += 1
        return maxh 


        