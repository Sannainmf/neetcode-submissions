class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        used = [[False] * len(grid[0]) for i in range(len(grid))]
        count = [0]

        def dfs(r, c):

            if r < 0 or r == len(grid):
                count[0] += 1
                return

            if c < 0 or c == len(grid[0]):
                count[0] += 1
                return

            if grid[r][c] == 0:
                count[0] += 1
                return

            if used[r][c]:
                return

            used[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shouldBreak = True
                    dfs(i, j)
                    return count[0]

            

        