class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        largest = 0
        
        while l < r:
            shortest = min(heights[l], heights[r])
            length = abs(l - r)
            largest = max(largest, shortest * length)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return largest


        