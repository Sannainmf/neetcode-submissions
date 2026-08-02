class Solution:
    def solve(self, board: List[List[str]]) -> None:

        """
        containing x and o

        connected horz and vert


        """
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        """
        containing x and o

        connected horz and vert
        """

        ROWS, COLS = len(board), len(board[0])
        seen = [[False] * COLS for i in range(ROWS)]

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return

            if seen[r][c]:
                return

            if board[r][c] == 'X':
                return

            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                edge[0] = True

            seen[r][c] = True
            region.append((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and not seen[i][j]:
                    edge = [False]
                    region = []
                    dfs(i, j)
                    if not edge[0]:
                        for r, c in region:
                            board[r][c] = 'X'