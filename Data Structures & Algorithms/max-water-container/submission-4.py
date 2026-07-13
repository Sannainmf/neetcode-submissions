class Solution:
    def maxArea(self, heights: List[int]) -> int:

        hash = {}
        k = 1
        biggest = 0
        

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = abs(i - j)
                if heights[i] < heights[j]:
                    height = heights[i]
                elif heights[i] > heights[j]:
                    height = heights[j]
                elif heights[i] == heights[j]:
                    height = heights[i]
                if j == i:
                    continue

                area = height * width
                hash[k] = area
                biggest = max(biggest, hash[k])

                k += 1
            
        return biggest

        
            

                

                






        


        
        