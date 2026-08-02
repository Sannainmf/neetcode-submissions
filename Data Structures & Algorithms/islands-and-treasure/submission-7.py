class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        """
        Thiis is going to a BFS
        """

        q = deque()
        seen = []   
        distance = 1

        def add(r, c):
            if r < 0 or r == len(grid):
                return

            if c < 0 or c == len(grid[0]):
                return

            if [r, c] in seen:
                return

            if grid[r][c] == -1:
                return

            q.append([r, c])
            seen.append([r, c])
            grid[r][c] = distance


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
                    seen.append([i, j])

        while q:

            for i in range(len(q)):
                r, c = q.popleft()

                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)

            distance += 1


        