class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        """
        water flows in 4 directions
        """
        res = []

        def pacific(r, c, prev):
            if r < 0 or c < 0:
                return True

            if r == len(heights) or c == len(heights[0]):
                return False

            if seen[r][c]:
                return False

            if heights[r][c] > prev:
                return False

            seen[r][c] = True
            cur = heights[r][c]

            return pacific(r + 1, c, cur) or pacific(r - 1, c, cur) or pacific(r, c + 1, cur) or pacific(r, c - 1, cur)
        
        def atlantic(r, c, prev):
            if r == len(heights) or c == len(heights[0]):
                return True

            if r < 0 or c < 0:
                return False

            if seen[r][c]:
                return False

            if heights[r][c] > prev:
                return False

            seen[r][c] = True
            cur = heights[r][c]

            return atlantic(r + 1, c, cur) or atlantic(r - 1, c, cur) or atlantic(r, c + 1, cur) or atlantic(r, c - 1, cur)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                seen = [[False] * len(heights[0]) for i in range(len(heights))]
                p = pacific(i, j, float('inf'))
                
                if p: 
                    seen = [[False] * len(heights[0]) for i in range(len(heights))]
                    a = atlantic(i, j, float('inf'))
                    if a and p:
                        res.append([i, j])

        return res


        