class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res, sol = [], []

        """
        we have 4 directions
        we cant go out of bounds
        we cant go to letter on same path, only remaining edges
        """ 

        used = [[False] * len(board[0]) for i in range(len(board))]

        def dfs(row, col, start):
            if len(sol) == len(word):
                res.append(''.join(sol[:]))
                return

            if start == len(word) - 1:
                sol.append(board[row][col])
                res.append(''.join(sol[:]))
                sol.pop()
                return
            
            if board[row][col] != word[start]:
                return

            if row > 0 and not used[row - 1][col]: #goes up
                sol.append(board[row][col])
                used[row][col] = True
                dfs(row - 1, col, start + 1)
                used[row][col] = False
                sol.pop()

            if row < len(board) - 1 and not used[row + 1][col]: #goes down
                sol.append(board[row][col])
                used[row][col] = True
                dfs(row + 1, col, start + 1)
                used[row][col] = False
                sol.pop()

            if col > 0 and not used[row][col - 1]:
                sol.append(board[row][col])
                used[row][col] = True
                dfs(row, col - 1, start + 1)
                used[row][col] = False
                sol.pop()

            if col < len(board[0]) - 1 and not used[row][col + 1]:
                sol.append(board[row][col])
                used[row][col] = True
                dfs(row, col + 1, start + 1)
                used[row][col] = False
                sol.pop()


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
        
        return word in res

        

        


            



        