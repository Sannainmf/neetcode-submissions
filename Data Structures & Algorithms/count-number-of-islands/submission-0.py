class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        used = [[False] * len(grid[0]) for i in range(len(grid))]

        def dfs(r, c):
            if r < 0 or r == len(grid):
                return

            if c < 0 or c == len(grid[0]):
                return

            if grid[r][c] == '0':
                return

            if used[r][c]:
                return

            used[r][c] = True

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not used[i][j]:
                    dfs(i, j)
                    count += 1

        return count


        