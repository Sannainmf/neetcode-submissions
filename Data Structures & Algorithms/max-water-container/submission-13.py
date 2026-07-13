class Solution:
    def maxArea(self, heights: List[int]) -> int:

        height = 0
        arr = []
        largest = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = j - i

                if heights[i] > heights[j]:
                    height = heights[j]
                elif heights[i] < heights[j]:
                    height = heights[i]
                elif heights[i] == heights[j]:
                    height = heights[i]

                area = width * height

                arr.append(area)


        for num in arr:
            largest = max(largest, num)


        return largest

            
