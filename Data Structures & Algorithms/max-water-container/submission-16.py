class Solution:
    def maxArea(self, heights: List[int]) -> int:

        arr = []

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = abs(j - i)

                if heights[i] > heights[j]:
                    length = heights[j]
                elif heights[i] < heights[j]:
                    length = heights[i]
                elif heights[i] == heights[j]:
                    length = heights[i]

                area = length * width

                arr.append(area)

        
        longest = 0

        for i in arr:
            longest = max(longest, i)

        return longest
            
