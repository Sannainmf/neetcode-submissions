class Solution:
    def maxArea(self, heights: List[int]) -> int:

        longest = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] < heights[j]:
                    height = heights[i]
                elif heights[i] > heights[j]:
                    height = heights[j]
                else:
                    height = heights[i]

                width = abs(i - j)

                area = height * width

                longest = max(longest, area)

        
        return longest



