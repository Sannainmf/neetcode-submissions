class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []

        def pacific(r, c, prev):
            if r < 0 or c < 0:
                return True

            if r == len(heights) or c == len(heights[0]):
                return False

            if [r, c] in seen:
                return False

            if heights[r][c] > prev:
                return False

            cur = heights[r][c]
            seen.append([r, c])

            return (
                pacific(r + 1, c, cur)
                or pacific(r - 1, c, cur)
                or pacific(r, c + 1, cur)
                or pacific(r, c - 1, cur)
            )

        def atlantic(r, c, prev):
            if r == len(heights) or c == len(heights[0]):
                return True

            if r < 0 or c < 0:
                return False

            if [r, c] in seen:
                return False

            if heights[r][c] > prev:
                return False

            cur = heights[r][c]
            seen.append([r, c])

            return (
                atlantic(r + 1, c, cur)
                or atlantic(r - 1, c, cur)
                or atlantic(r, c + 1, cur)
                or atlantic(r, c - 1, cur)
            )

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                seen = []
                if atlantic(i, j, float("inf")):
                    seen = []
                    if pacific(i, j, float('inf')):
                        res.append([i, j])

        return res
