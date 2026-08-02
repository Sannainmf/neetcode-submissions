class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        """
        grid[i] is either 0 or 1.

        an island has group of 1s cnnected horizontally and veritclly

        area of island is number of cells within island (inc by 1)

        find max area on grid, if no island exists return 0

        just dfs every time u find one and return count, update max
        """

        area = [0]

        def dfs(r, c):
            if r < 0 or r == len(grid):
                return

            if c < 0 or c == len(grid[0]):
                return

            if grid[r][c] == 0:
                return

            if seen[r][c]:
                return

            if grid[r][c] == 1:
                priv[0] += 1
                seen[r][c] = True

            area[0] = max(area[0], priv[0])

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    priv = [0]
                    seen = [[False] * len(grid[0]) for i in range(len(grid))]
                    dfs(i, j)
                    area[0] = max(area[0], priv[0])

                    
        return area[0]

        


        