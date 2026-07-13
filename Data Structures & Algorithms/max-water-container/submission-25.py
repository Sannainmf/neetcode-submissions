class Solution:
    def maxArea(self, heights: List[int]) -> int:

        largest = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                if heights[j] > heights[i]:
                    height = heights[i]
                elif heights[i] > heights[j]:
                    height = heights[j]
                else:
                    height = heights[i]

                length = abs(j - i)

                area = height * length

                largest = max(largest, area)

        return largest

