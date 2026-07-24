class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res, sol = [], []
        seen = [[False] * len(board[0]) for i in range(len(board))]

        def dfs(r, c, i):

            if i == len(word):
                res.append(''.join(sol[:]))
                return
                
            if r < 0 or r == len(board):
                return

            if c < 0 or c == len(board[0]):
                return

            if board[r][c] != word[i]:
                return

            if seen[r][c]:
                return
                

            sol.append(board[r][c])
            seen[r][c] = True

            dfs(r + 1, c, i + 1)
            dfs(r - 1, c, i + 1)
            dfs(r, c + 1, i + 1)
            dfs(r, c - 1, i + 1)

            sol.pop()
            seen[r][c] = False

            

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char == word[0]:
                    dfs(i, j, 0)

        return word in res
        

        