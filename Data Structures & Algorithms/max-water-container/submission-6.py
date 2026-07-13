class Solution:
    def maxArea(self, heights: List[int]) -> int:

        hash = {}
        k = 1
        greatest = 0 

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = abs(i - j)
                if heights[i] > heights[j]:
                    length = heights[j]
                elif heights[i] < heights[j]:
                    length = heights[i]
                elif heights[i] == heights[j]:
                    length = heights[i]

                if i == j:
                    continue
                
                area = length * width
                greatest = max(greatest, area)
                hash[k] = area
                k += 1

        return greatest

