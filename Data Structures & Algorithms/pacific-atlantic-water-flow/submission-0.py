class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(r, c, prev, pacific, vis):
            if [r, c] in vis:
                return False

            if r < 0 or c < 0:
                return pacific

            if r == len(heights) or c == len(heights[0]):
                return not pacific
            
            if heights[r][c] > prev:
                return False

            h = heights[r][c]
            vis.append([r, c])

            return dfs(r - 1, c, h, pacific, vis) or dfs(r, c - 1, h, pacific, vis) or dfs(r + 1, c, h, pacific, vis) or dfs(r, c + 1, h, pacific, vis)
                
        arr = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i, j, float('inf'), True, []) and dfs(i, j, float('inf'), False, []):
                    arr.append([i, j])

        return arr
        